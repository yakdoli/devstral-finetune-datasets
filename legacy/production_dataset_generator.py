#!/usr/bin/env python3
"""
Production-Ready Syncfusion Dataset Generator for Devstral Fine-tuning
Final version with optimized error handling, batch processing, and progress tracking
"""

import json
import asyncio
import aiohttp
import aiofiles
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
import logging
import re
import argparse
from datetime import datetime
import time

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('dataset_generation.log'),
        logging.StreamHandler()
    ]
)
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
    max_tokens: int = 24000
    temperature: float = 0.2
    max_concurrent: int = 6
    batch_size: int = 12
    retry_attempts: int = 2

@dataclass
class ProcessingStats:
    """Statistics for tracking generation progress"""
    total_pages: int = 0
    processed_pages: int = 0
    successful_pages: int = 0
    total_samples: int = 0
    start_time: float = 0
    errors: List[str] = None
    
    def __post_init__(self):
        if self.errors is None:
            self.errors = []

class ProductionDatasetGenerator:
    """Production-ready dataset generator with comprehensive error handling"""
    
    def __init__(self, config: ProcessingConfig):
        self.config = config
        self.session: Optional[aiohttp.ClientSession] = None
        self.stats = ProcessingStats()
        
    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=180)
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    def clean_json_content(self, content: str) -> str:
        """Advanced JSON content cleaning"""
        # Remove markdown blocks
        content = re.sub(r'```(?:json)?\s*', '', content, flags=re.IGNORECASE)
        content = re.sub(r'```\s*$', '', content)
        
        # Remove control characters
        content = re.sub(r'[\x00-\x08\x0b-\x0c\x0e-\x1f\x7f-\x9f]', '', content)
        
        # Fix common JSON issues
        content = re.sub(r'([^\\])\\([^"\\\/bfnrtu])', r'\1\\\\\2', content)
        content = re.sub(r'"\s*\+\s*"', '', content)  # Remove string concatenation
        
        return content.strip()

    def extract_qa_objects(self, content: str) -> List[Dict[str, str]]:
        """Extract Q&A objects using multiple strategies"""
        objects = []
        
        # Strategy 1: Look for complete JSON array
        try:
            cleaned = self.clean_json_content(content)
            start = cleaned.find('[')
            end = cleaned.rfind(']') + 1
            
            if start != -1 and end > start:
                json_str = cleaned[start:end]
                parsed = json.loads(json_str)
                if isinstance(parsed, list):
                    return [obj for obj in parsed if isinstance(obj, dict)]
        except:
            pass
        
        # Strategy 2: Extract individual objects with regex
        pattern = r'\{\s*"instruction"\s*:\s*"([^"]*(?:\\.[^"]*)*)"\s*,\s*"input"\s*:\s*"([^"]*(?:\\.[^"]*)*)"\s*,\s*"output"\s*:\s*"([^"]*(?:\\.[^"]*)*)"[^}]*\}'
        for match in re.finditer(pattern, content, re.DOTALL):
            try:
                obj = {
                    "instruction": match.group(1).replace('\\"', '"'),
                    "input": match.group(2).replace('\\"', '"'),
                    "output": match.group(3).replace('\\"', '"')
                }
                objects.append(obj)
            except:
                continue
        
        return objects

    async def generate_qa_pairs_with_retry(self, content: str, page_info: Dict[str, Any]) -> List[UnslothSample]:
        """Generate Q&A pairs with retry logic"""
        
        for attempt in range(self.config.retry_attempts + 1):
            try:
                samples = await self._generate_qa_pairs(content, page_info, attempt)
                if samples:
                    return samples
                    
                if attempt < self.config.retry_attempts:
                    await asyncio.sleep(1)  # Brief delay between retries
                    
            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed: {e}")
                if attempt < self.config.retry_attempts:
                    await asyncio.sleep(2)
                
        return []

    async def _generate_qa_pairs(self, content: str, page_info: Dict[str, Any], attempt: int) -> List[UnslothSample]:
        """Internal method for generating Q&A pairs"""
        
        # Adjust temperature based on attempt
        temperature = self.config.temperature + (attempt * 0.1)
        
        system_prompt = """You are creating training data for a code assistant. Generate exactly 3 Q&A pairs from the Syncfusion documentation.

STRICT REQUIREMENTS:
- Return ONLY valid JSON array
- Each output must be 150-400 characters
- Include practical code examples
- Focus on implementation details

EXACT FORMAT:
[{"instruction":"specific question","input":"","output":"concise answer with code if relevant"},{"instruction":"another question","input":"","output":"practical answer"},{"instruction":"third question","input":"","output":"implementation focused answer"}]"""

        # Truncate content to avoid token limits
        truncated_content = content[:1500] if len(content) > 1500 else content
        
        user_prompt = f"Documentation:\n{truncated_content}\n\nGenerate 3 Q&A pairs in exact JSON format."

        try:
            payload = {
                "model": self.config.model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "max_tokens": min(self.config.max_tokens, 20000),
                "temperature": min(temperature, 0.5)
            }
            
            async with self.session.post(
                f"{self.config.endpoint}/chat/completions",
                json=payload,
                headers={"Content-Type": "application/json"}
            ) as response:
                
                if response.status != 200:
                    logger.error(f"API error {response.status} on attempt {attempt + 1}")
                    return []
                
                result = await response.json()
                raw_content = result["choices"][0]["message"]["content"]
                
                # Extract Q&A objects
                qa_objects = self.extract_qa_objects(raw_content)
                
                samples = []
                for qa in qa_objects[:3]:  # Limit to 3 samples
                    if all(key in qa for key in ["instruction", "output"]):
                        samples.append(UnslothSample(
                            instruction=qa["instruction"].strip()[:500],  # Limit length
                            input=qa.get("input", "").strip(),
                            output=qa["output"].strip()[:1000]  # Limit length
                        ))
                
                return samples
                    
        except Exception as e:
            logger.error(f"Generation error on attempt {attempt + 1}: {e}")
            return []

    async def process_page(self, md_path: Path, json_path: Path) -> List[UnslothSample]:
        """Process a single page with error handling"""
        try:
            # Read files
            async with aiofiles.open(md_path, 'r', encoding='utf-8') as f:
                md_content = await f.read()
            
            if not md_content.strip():
                return []
            
            async with aiofiles.open(json_path, 'r', encoding='utf-8') as f:
                page_info = json.loads(await f.read())
            
            # Generate samples
            samples = await self.generate_qa_pairs_with_retry(md_content, page_info)
            
            # Update stats
            self.stats.processed_pages += 1
            if samples:
                self.stats.successful_pages += 1
                self.stats.total_samples += len(samples)
            
            logger.info(f"Page {md_path.name}: {len(samples)} samples (Success: {self.stats.successful_pages}/{self.stats.processed_pages})")
            return samples
            
        except Exception as e:
            error_msg = f"Error processing {md_path.name}: {e}"
            logger.error(error_msg)
            self.stats.errors.append(error_msg)
            return []

    async def process_section_batch(self, section_path: Path, max_pages: Optional[int] = None) -> List[UnslothSample]:
        """Process a section with batch control"""
        
        md_files = list(section_path.glob("page_*.md"))
        md_files.sort()
        
        if max_pages:
            md_files = md_files[:max_pages]
        
        self.stats.total_pages += len(md_files)
        all_samples = []
        
        # Process in controlled batches
        semaphore = asyncio.Semaphore(self.config.max_concurrent)
        
        async def process_with_semaphore(md_file):
            async with semaphore:
                json_file = md_file.with_suffix('.json')
                if json_file.exists():
                    return await self.process_page(md_file, json_file)
                return []
        
        # Process in batches to manage memory and connections
        for i in range(0, len(md_files), self.config.batch_size):
            batch = md_files[i:i + self.config.batch_size]
            
            logger.info(f"Processing batch {i//self.config.batch_size + 1}/{(len(md_files)-1)//self.config.batch_size + 1}")
            
            tasks = [process_with_semaphore(md_file) for md_file in batch]
            batch_results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for result in batch_results:
                if isinstance(result, Exception):
                    logger.error(f"Batch processing error: {result}")
                    continue
                all_samples.extend(result)
            
            # Brief pause between batches
            await asyncio.sleep(0.5)
        
        return all_samples

    async def generate_full_dataset(self, sections: List[str], max_pages_per_section: Optional[int] = None) -> List[Dict[str, Any]]:
        """Generate complete dataset"""
        
        self.stats.start_time = time.time()
        md_staging = Path("md_staging")
        
        if not md_staging.exists():
            raise ValueError("md_staging directory not found")
        
        available_sections = [d.name for d in md_staging.iterdir() if d.is_dir()]
        valid_sections = [s for s in sections if s in available_sections]
        
        logger.info(f"Processing sections: {valid_sections}")
        logger.info(f"Max pages per section: {max_pages_per_section or 'All'}")
        
        all_samples = []
        
        for section in valid_sections:
            section_path = md_staging / section
            logger.info(f"Starting section: {section}")
            
            section_samples = await self.process_section_batch(section_path, max_pages_per_section)
            all_samples.extend(section_samples)
            
            logger.info(f"Section {section} complete: {len(section_samples)} samples")
        
        # Final statistics
        elapsed = time.time() - self.stats.start_time
        success_rate = (self.stats.successful_pages / self.stats.processed_pages * 100) if self.stats.processed_pages > 0 else 0
        
        logger.info(f"Generation complete!")
        logger.info(f"Total time: {elapsed:.1f}s")
        logger.info(f"Pages processed: {self.stats.processed_pages}")
        logger.info(f"Success rate: {success_rate:.1f}%")
        logger.info(f"Total samples: {len(all_samples)}")
        
        return [asdict(sample) for sample in all_samples]

async def main():
    """Main execution function"""
    
    parser = argparse.ArgumentParser(description="Production Syncfusion Dataset Generator")
    parser.add_argument("--sections", nargs="+", default=["calculate", "chart", "grid", "edit"],
                       help="Sections to process")
    parser.add_argument("--max-pages", type=int, help="Max pages per section")
    parser.add_argument("--output", default="syncfusion_production_dataset.json",
                       help="Output file")
    parser.add_argument("--concurrent", type=int, default=6, help="Max concurrent requests")
    parser.add_argument("--batch-size", type=int, default=12, help="Batch size")
    
    args = parser.parse_args()
    
    config = ProcessingConfig(
        max_concurrent=args.concurrent,
        batch_size=args.batch_size
    )
    
    try:
        async with ProductionDatasetGenerator(config) as generator:
            dataset = await generator.generate_full_dataset(args.sections, args.max_pages)
            
            # Save dataset
            output_path = Path(args.output)
            async with aiofiles.open(output_path, 'w', encoding='utf-8') as f:
                await f.write(json.dumps(dataset, indent=2, ensure_ascii=False))
            
            # Save statistics
            stats_data = {
                "generation_time": datetime.now().isoformat(),
                "total_samples": len(dataset),
                "sections_processed": len(args.sections),
                "pages_processed": generator.stats.processed_pages,
                "success_rate": f"{(generator.stats.successful_pages / generator.stats.processed_pages * 100):.1f}%" if generator.stats.processed_pages > 0 else "0%",
                "errors": generator.stats.errors[:10]  # Save first 10 errors
            }
            
            stats_path = output_path.with_suffix('.stats.json')
            async with aiofiles.open(stats_path, 'w', encoding='utf-8') as f:
                await f.write(json.dumps(stats_data, indent=2, ensure_ascii=False))
            
            print(f"\nDataset saved: {output_path}")
            print(f"Statistics saved: {stats_path}")
            
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())