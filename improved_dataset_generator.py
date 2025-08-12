#!/usr/bin/env python3
"""
Improved Syncfusion Dataset Generator with better error handling and JSON parsing
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
import re

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
    max_tokens: int = 32000
    temperature: float = 0.25
    max_concurrent: int = 4

class ImprovedDatasetGenerator:
    """Improved dataset generator with better error handling"""
    
    def __init__(self, config: ProcessingConfig):
        self.config = config
        self.session: Optional[aiohttp.ClientSession] = None
        
    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=120)
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    def clean_json_content(self, content: str) -> str:
        """Clean and prepare JSON content for parsing"""
        # Remove markdown code blocks
        content = re.sub(r'```json\s*', '', content)
        content = re.sub(r'```\s*$', '', content)
        
        # Remove control characters but preserve newlines in strings
        content = re.sub(r'[\x00-\x08\x0b-\x0c\x0e-\x1f\x7f-\x9f]', '', content)
        
        # Fix common JSON issues
        content = re.sub(r'([^\\])\\([^"\\\/bfnrtux])', r'\1\\\\\2', content)  # Fix unescaped backslashes
        content = re.sub(r'"\s*\n\s*"', '" + "', content)  # Handle line breaks in strings
        
        return content.strip()

    def extract_json_objects(self, content: str) -> List[Dict[str, Any]]:
        """Extract JSON objects even if the overall structure is malformed"""
        objects = []
        
        # Find individual objects with instruction/output pattern
        pattern = r'\{\s*"instruction"\s*:\s*"([^"]*)"[^}]*"output"\s*:\s*"([^"]*(?:\\.[^"]*)*)"[^}]*\}'
        matches = re.finditer(pattern, content, re.DOTALL)
        
        for match in matches:
            try:
                obj_str = match.group(0)
                # Try to parse this individual object
                obj = json.loads(obj_str)
                objects.append(obj)
            except json.JSONDecodeError:
                continue
        
        return objects

    async def generate_qa_pairs(self, content: str, page_info: Dict[str, Any]) -> List[UnslothSample]:
        """Generate Q&A pairs with improved error handling"""
        
        system_prompt = """You are an expert at creating high-quality training data for code assistant fine-tuning.
Generate exactly 3 question-answer pairs from the given Syncfusion WinForms documentation.

CRITICAL: Return ONLY valid JSON. No markdown blocks, no explanations.

Format (exact structure required):
[{"instruction":"question here","input":"","output":"detailed answer here"},{"instruction":"question here","input":"","output":"detailed answer here"},{"instruction":"question here","input":"","output":"detailed answer here"}]

Requirements:
- Each output should be 200-500 characters  
- Focus on practical implementation details
- Include code examples when relevant
- Use proper JSON escaping for quotes and backslashes"""

        user_prompt = f"""Documentation: {content[:2000]}

Generate 3 Q&A pairs in the exact JSON format specified."""

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
                raw_content = result["choices"][0]["message"]["content"]
                
                # Try multiple parsing strategies
                samples = []
                
                # Strategy 1: Standard JSON parsing
                try:
                    cleaned = self.clean_json_content(raw_content)
                    json_start = cleaned.find('[')
                    json_end = cleaned.rfind(']') + 1
                    
                    if json_start != -1 and json_end > json_start:
                        json_content = cleaned[json_start:json_end]
                        qa_data = json.loads(json_content)
                        
                        for qa in qa_data:
                            if isinstance(qa, dict) and "instruction" in qa and "output" in qa:
                                samples.append(UnslothSample(
                                    instruction=qa.get("instruction", "").strip(),
                                    input=qa.get("input", "").strip(), 
                                    output=qa.get("output", "").strip()
                                ))
                        
                        if samples:
                            return samples
                
                except json.JSONDecodeError:
                    pass
                
                # Strategy 2: Extract individual objects
                try:
                    objects = self.extract_json_objects(raw_content)
                    for obj in objects:
                        if "instruction" in obj and "output" in obj:
                            samples.append(UnslothSample(
                                instruction=obj.get("instruction", "").strip(),
                                input=obj.get("input", "").strip(),
                                output=obj.get("output", "").strip()
                            ))
                    
                    if samples:
                        return samples
                        
                except Exception:
                    pass
                
                logger.error(f"All parsing strategies failed for page {page_info.get('page_number', 'unknown')}")
                return []
                    
        except Exception as e:
            logger.error(f"Error generating Q&A pairs: {e}")
            return []

    async def process_page(self, md_path: Path, json_path: Path) -> List[UnslothSample]:
        """Process a single documentation page"""
        try:
            async with aiofiles.open(md_path, 'r', encoding='utf-8') as f:
                md_content = await f.read()
            
            async with aiofiles.open(json_path, 'r', encoding='utf-8') as f:
                page_info = json.loads(await f.read())
            
            samples = await self.generate_qa_pairs(md_content, page_info)
            
            logger.info(f"Generated {len(samples)} samples from {md_path.name}")
            return samples
            
        except Exception as e:
            logger.error(f"Error processing {md_path}: {e}")
            return []

async def run_improved_test():
    """Run improved test generation"""
    
    config = ProcessingConfig(
        max_tokens=16000,
        temperature=0.2,
        max_concurrent=3
    )
    
    md_staging = Path("md_staging/calculate")
    output_file = Path("improved_test_dataset.json")
    
    if not md_staging.exists():
        print("md_staging/calculate directory not found")
        return
    
    async with ImprovedDatasetGenerator(config) as generator:
        all_samples = []
        
        # Process first 8 pages
        md_files = list(md_staging.glob("page_*.md"))[:8]
        
        for md_file in md_files:
            json_file = md_file.with_suffix('.json')
            if json_file.exists():
                samples = await generator.process_page(md_file, json_file)
                all_samples.extend(samples)
                print(f"+ {md_file.name}: {len(samples)} samples")
        
        # Save results
        dataset = [asdict(s) for s in all_samples]
        
        async with aiofiles.open(output_file, 'w', encoding='utf-8') as f:
            await f.write(json.dumps(dataset, indent=2, ensure_ascii=False))
        
        print(f"\nImproved test complete!")
        print(f"Total samples: {len(all_samples)}")
        print(f"Success rate: {len([s for s in all_samples if s.instruction])}/{len(md_files)}")
        print(f"Output saved to: {output_file}")

if __name__ == "__main__":
    asyncio.run(run_improved_test())