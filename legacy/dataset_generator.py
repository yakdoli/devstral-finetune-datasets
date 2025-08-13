#!/usr/bin/env python3
"""
Syncfusion User Guide Dataset Generator for Devstral Fine-tuning
Uses Qwen2.5-VL local LLM with SGLang backend for efficient batch processing
"""

import json
import os
import asyncio
import aiohttp
import aiofiles
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
from datetime import datetime
import logging
import argparse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class UnslothSample:
    """Unsloth dataset format for fine-tuning"""
    instruction: str
    input: str
    output: str
    
@dataclass
class ProcessingConfig:
    """Configuration for dataset generation"""
    endpoint: str = "http://123.37.28.120:9997/v1"
    model: str = "qwen2.5-vl-instruct"
    max_tokens: int = 128000
    temperature: float = 0.3
    max_concurrent: int = 8
    batch_size: int = 16

class SyncfusionDatasetGenerator:
    """Main class for generating Unsloth datasets from Syncfusion documentation"""
    
    def __init__(self, config: ProcessingConfig):
        self.config = config
        self.session: Optional[aiohttp.ClientSession] = None
        
    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=300)
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def generate_qa_pairs(self, content: str, page_info: Dict[str, Any]) -> List[UnslothSample]:
        """Generate Q&A pairs from documentation content using local LLM"""
        
        # System prompt for generating training data
        system_prompt = """You are an expert at creating high-quality training data for code assistant fine-tuning. 
Generate diverse question-answer pairs from the given Syncfusion WinForms documentation.

Create 3-5 Q&A pairs that cover:
1. Conceptual understanding (what is X, how does Y work)
2. Implementation guidance (how to implement/use feature)  
3. Code examples and best practices
4. Troubleshooting and common issues
5. API reference and parameters

IMPORTANT: Return ONLY a valid JSON array, no extra text or explanations.

Example format:
[
  {
    "instruction": "How to implement basic Essential Calculate functionality in WinForms?",
    "input": "",
    "output": "To implement Essential Calculate in WinForms, you need to: [detailed step-by-step answer with code examples]"
  }
]

Focus on practical developer questions that would benefit from this documentation. Return only the JSON array."""

        user_prompt = f"""
Documentation Content:
{content}

Page Info:
- Product: {page_info.get('product', 'Syncfusion WinForms')}
- Component: {page_info.get('document_name', 'Unknown')}
- Version: {page_info.get('version', 'Unknown')}
- Page: {page_info.get('page_number', 'Unknown')}

Generate training Q&A pairs from this content.
"""

        try:
            payload = {
                "model": self.config.model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "max_tokens": self.config.max_tokens,
                "temperature": self.config.temperature
            }
            
            async with self.session.post(
                f"{self.config.endpoint}/chat/completions",
                json=payload,
                headers={"Content-Type": "application/json"}
            ) as response:
                if response.status != 200:
                    logger.error(f"API error: {response.status}")
                    return []
                
                result = await response.json()
                content = result["choices"][0]["message"]["content"]
                
                # Parse JSON response
                try:
                    # Extract JSON from response if it's wrapped in markdown or other text
                    json_start = content.find('[')
                    json_end = content.rfind(']') + 1
                    
                    if json_start != -1 and json_end > json_start:
                        json_content = content[json_start:json_end]
                        
                        # Clean control characters and normalize whitespace
                        import re
                        json_content = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', json_content)  # Remove control chars
                        json_content = re.sub(r'\s+', ' ', json_content)  # Normalize whitespace
                        
                        qa_data = json.loads(json_content)
                        
                        samples = []
                        for qa in qa_data:
                            if isinstance(qa, dict):
                                samples.append(UnslothSample(
                                    instruction=qa.get("instruction", ""),
                                    input=qa.get("input", ""),
                                    output=qa.get("output", "")
                                ))
                        return samples
                    else:
                        logger.error("No JSON array found in response")
                        return []
                        
                except json.JSONDecodeError as e:
                    logger.error(f"Failed to parse JSON response: {e}")
                    logger.error(f"Content: {content[:500]}...")
                    return []
                    
        except Exception as e:
            logger.error(f"Error generating Q&A pairs: {e}")
            return []

    async def process_page(self, md_path: Path, json_path: Path) -> List[UnslothSample]:
        """Process a single documentation page"""
        try:
            # Read markdown content
            async with aiofiles.open(md_path, 'r', encoding='utf-8') as f:
                md_content = await f.read()
            
            # Read JSON metadata
            async with aiofiles.open(json_path, 'r', encoding='utf-8') as f:
                page_info = json.loads(await f.read())
            
            # Generate Q&A pairs
            samples = await self.generate_qa_pairs(md_content, page_info)
            
            logger.info(f"Generated {len(samples)} samples from {md_path.name}")
            return samples
            
        except Exception as e:
            logger.error(f"Error processing {md_path}: {e}")
            return []

    async def process_section(self, section_path: Path) -> List[UnslothSample]:
        """Process all pages in a documentation section"""
        all_samples = []
        
        # Find all MD/JSON pairs
        md_files = list(section_path.glob("page_*.md"))
        md_files.sort()
        
        # Process in batches with concurrency control
        semaphore = asyncio.Semaphore(self.config.max_concurrent)
        
        async def process_with_semaphore(md_file):
            async with semaphore:
                json_file = md_file.with_suffix('.json')
                if json_file.exists():
                    return await self.process_page(md_file, json_file)
                return []
        
        # Process pages in batches
        for i in range(0, len(md_files), self.config.batch_size):
            batch = md_files[i:i + self.config.batch_size]
            logger.info(f"Processing batch {i//self.config.batch_size + 1}: {len(batch)} pages")
            
            tasks = [process_with_semaphore(md_file) for md_file in batch]
            batch_results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for result in batch_results:
                if isinstance(result, Exception):
                    logger.error(f"Batch processing error: {result}")
                    continue
                all_samples.extend(result)
        
        return all_samples

    async def generate_dataset(self, 
                             md_staging_path: Path, 
                             output_path: Path,
                             sections: Optional[List[str]] = None):
        """Generate complete Unsloth dataset from all sections"""
        
        all_samples = []
        available_sections = [d.name for d in md_staging_path.iterdir() if d.is_dir()]
        
        if sections is None:
            sections = available_sections
        else:
            sections = [s for s in sections if s in available_sections]
        
        logger.info(f"Processing sections: {sections}")
        
        for section in sections:
            section_path = md_staging_path / section
            logger.info(f"Processing section: {section}")
            
            section_samples = await self.process_section(section_path)
            all_samples.extend(section_samples)
            
            logger.info(f"Section {section}: {len(section_samples)} samples")
        
        # Save dataset
        dataset_data = [asdict(sample) for sample in all_samples]
        
        async with aiofiles.open(output_path, 'w', encoding='utf-8') as f:
            await f.write(json.dumps(dataset_data, indent=2, ensure_ascii=False))
        
        logger.info(f"Dataset saved: {output_path}")
        logger.info(f"Total samples: {len(all_samples)}")
        
        return dataset_data

async def main():
    parser = argparse.ArgumentParser(description="Generate Unsloth dataset from Syncfusion docs")
    parser.add_argument("--md-staging", default="md_staging", 
                       help="Path to md_staging directory")
    parser.add_argument("--output", default="syncfusion_unsloth_dataset.json",
                       help="Output dataset file")
    parser.add_argument("--sections", nargs="*", 
                       help="Specific sections to process (default: all)")
    parser.add_argument("--endpoint", default="http://123.37.28.120:9997/v1",
                       help="LLM API endpoint")
    parser.add_argument("--max-concurrent", type=int, default=8,
                       help="Max concurrent requests")
    parser.add_argument("--batch-size", type=int, default=16,
                       help="Batch size for processing")
    
    args = parser.parse_args()
    
    config = ProcessingConfig(
        endpoint=args.endpoint,
        max_concurrent=args.max_concurrent,
        batch_size=args.batch_size
    )
    
    md_staging_path = Path(args.md_staging)
    output_path = Path(args.output)
    
    if not md_staging_path.exists():
        logger.error(f"md_staging path does not exist: {md_staging_path}")
        return
    
    async with SyncfusionDatasetGenerator(config) as generator:
        await generator.generate_dataset(md_staging_path, output_path, args.sections)

if __name__ == "__main__":
    asyncio.run(main())