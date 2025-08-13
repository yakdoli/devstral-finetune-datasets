#!/usr/bin/env python3
"""
Quick test runner for validating the dataset generation pipeline
"""

import asyncio
import json
import logging
from pathlib import Path
from dataset_generator import SyncfusionDatasetGenerator, ProcessingConfig

async def quick_test():
    """Run generation for a small sample of pages"""
    
    config = ProcessingConfig(
        endpoint="http://123.37.28.120:9997/v1",
        model="qwen2.5-vl-instruct",
        max_tokens=16000,
        temperature=0.25,
        max_concurrent=3,  # Conservative for testing
        batch_size=6
    )
    
    md_staging = Path("md_staging")
    output_file = Path("quick_test_dataset.json")
    
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting quick test with limited pages...")
    
    # Process only calculate section for now
    sections = ["calculate"]
    
    async with SyncfusionDatasetGenerator(config) as generator:
        
        # Process first few pages only
        calculate_path = md_staging / "calculate"
        md_files = list(calculate_path.glob("page_*.md"))[:10]  # First 10 pages only
        
        all_samples = []
        for md_file in md_files:
            json_file = md_file.with_suffix('.json')
            if json_file.exists():
                samples = await generator.process_page(md_file, json_file)
                all_samples.extend(samples)
                print(f"Processed {md_file.name}: {len(samples)} samples")
        
        # Save results
        dataset_data = [{"instruction": s.instruction, "input": s.input, "output": s.output} for s in all_samples]
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(dataset_data, f, indent=2, ensure_ascii=False)
        
        print(f"Quick test complete: {len(all_samples)} total samples saved to {output_file}")
        
        # Show stats
        if all_samples:
            avg_instruction_len = sum(len(s.instruction) for s in all_samples) / len(all_samples)
            avg_output_len = sum(len(s.output) for s in all_samples) / len(all_samples)
            print(f"Average instruction length: {avg_instruction_len:.0f} chars")
            print(f"Average output length: {avg_output_len:.0f} chars")

if __name__ == "__main__":
    asyncio.run(quick_test())