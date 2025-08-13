#!/usr/bin/env python3
"""
Production runner for Syncfusion dataset generation with enhanced prompt caching and batching
"""

import asyncio
import json
import logging
from pathlib import Path
from dataset_generator import SyncfusionDatasetGenerator, ProcessingConfig

async def run_full_generation():
    """Run complete dataset generation with optimized settings"""
    
    # Production configuration with optimized settings for SGLang
    config = ProcessingConfig(
        endpoint="http://123.37.28.120:9997/v1",
        model="qwen2.5-vl-instruct",
        max_tokens=32000,  # Reduced for better throughput
        temperature=0.3,
        max_concurrent=12,  # Increased for better parallelism
        batch_size=24      # Larger batches for efficiency
    )
    
    md_staging = Path("md_staging")
    output_file = Path("syncfusion_dataset_full.json")
    
    logging.info("Starting full dataset generation...")
    logging.info(f"Configuration: {config}")
    
    async with SyncfusionDatasetGenerator(config) as generator:
        dataset = await generator.generate_dataset(
            md_staging_path=md_staging,
            output_path=output_file
        )
    
    # Generate summary statistics
    stats = {
        "total_samples": len(dataset),
        "sections_processed": len([d for d in md_staging.iterdir() if d.is_dir()]),
        "avg_instruction_length": sum(len(s["instruction"]) for s in dataset) / len(dataset) if dataset else 0,
        "avg_output_length": sum(len(s["output"]) for s in dataset) / len(dataset) if dataset else 0
    }
    
    stats_file = Path("dataset_stats.json")
    with open(stats_file, 'w') as f:
        json.dump(stats, f, indent=2)
    
    logging.info(f"Generation complete. Statistics saved to {stats_file}")
    return dataset

async def run_selective_generation():
    """Run generation for specific high-value sections first"""
    
    # Priority sections for initial testing
    priority_sections = ["calculate", "chart", "grid", "edit"]
    
    config = ProcessingConfig(
        endpoint="http://123.37.28.120:9997/v1",
        model="qwen2.5-vl-instruct",
        max_tokens=64000,  # Higher for quality samples
        temperature=0.2,   # Lower for more consistent output
        max_concurrent=6,  # Conservative for testing
        batch_size=12
    )
    
    md_staging = Path("md_staging")
    output_file = Path("syncfusion_dataset_priority.json")
    
    logging.info(f"Starting selective generation for: {priority_sections}")
    
    async with SyncfusionDatasetGenerator(config) as generator:
        dataset = await generator.generate_dataset(
            md_staging_path=md_staging,
            output_path=output_file,
            sections=priority_sections
        )
    
    logging.info(f"Priority generation complete: {len(dataset)} samples")
    return dataset

if __name__ == "__main__":
    import sys
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    if len(sys.argv) > 1 and sys.argv[1] == "full":
        asyncio.run(run_full_generation())
    else:
        asyncio.run(run_selective_generation())