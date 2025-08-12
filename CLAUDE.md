# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains a Syncfusion user guide dataset generation pipeline for fine-tuning Devstral models. The project processes OCR-extracted Syncfusion WinForms documentation and converts it into Unsloth-compatible training datasets using a local Qwen2.5-VL model with SGLang backend.

## Key Architecture

### Data Structure
- `md_staging/`: Contains section-based documentation pages (calculate, chart, grid, edit, etc.)
  - Each section has `page_XXX.md` (OCR content) and `page_XXX.json` (metadata) pairs
  - Pages contain structured markdown with API documentation, code examples, and usage instructions
- `output/`: Contains consolidated documentation files per section (e.g., `calculate_process_isolated.md`)

### Core Components
- `dataset_generator.py`: Main async pipeline for generating Q&A training pairs
- `prompt_cache_optimizer.py`: SGLang-specific caching and batch optimization
- `run_dataset_generation.py`: Production runner with optimized configurations

### LLM Integration
- Local endpoint: `http://123.37.28.120:9997/v1` (Qwen2.5-VL + SGLang)
- Supports OpenAI-compatible chat completions API
- Implements prompt caching for system prompt reuse
- Batch processing with configurable concurrency limits

## Common Development Commands

### Dataset Generation
```bash
# Install dependencies
pip install -r requirements.txt

# Generate priority sections dataset (recommended for testing)
python run_dataset_generation.py

# Generate full dataset (all sections)
python run_dataset_generation.py full

# Custom generation with specific sections
python dataset_generator.py --sections calculate chart grid --max-concurrent 6 --batch-size 12

# Generate with custom endpoint
python dataset_generator.py --endpoint http://localhost:8000/v1 --output custom_dataset.json
```

### Testing and Validation
```bash
# Test LLM endpoint connectivity
curl -X POST "http://123.37.28.120:9997/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -d '{"model": "qwen2.5-vl-instruct", "messages": [{"role": "user", "content": "Test"}], "max_tokens": 10}'

# Validate dataset format
python -c "import json; data=json.load(open('syncfusion_dataset_priority.json')); print(f'Samples: {len(data)}'); print(f'Keys: {set(data[0].keys()) if data else \"empty\"}')"
```

## Processing Configuration

### Optimal Settings
- **Production**: `max_concurrent=12`, `batch_size=24`, `max_tokens=32000`
- **Testing**: `max_concurrent=6`, `batch_size=12`, `max_tokens=64000`
- **Quality Focus**: `temperature=0.2`, higher max_tokens for detailed responses
- **Speed Focus**: `temperature=0.3`, lower max_tokens, higher concurrency

### Memory Management
- SGLang backend supports prompt caching via shared system prompts
- Batch processing reduces API overhead and improves throughput
- Use `ProcessingConfig` class to manage all parameters centrally

## Data Format

### Input Structure (md_staging)
```
md_staging/
├── calculate/
│   ├── page_001.md    # OCR markdown content
│   ├── page_001.json  # Page metadata
│   └── ...
├── chart/
└── grid/
```

### Output Format (Unsloth)
```json
[
  {
    "instruction": "How to implement Essential Calculate in WinForms?",
    "input": "",
    "output": "To implement Essential Calculate: [step-by-step guide with code]"
  }
]
```

## Important Notes

### Quality Control
- Each page generates 3-5 Q&A pairs covering conceptual, implementation, API, and troubleshooting aspects
- System prompts are optimized for Syncfusion WinForms context
- Temperature settings balance consistency (0.2) vs creativity (0.3)

### Performance Optimization
- Use `prompt_cache_optimizer.py` for efficient system prompt reuse
- Implement proper error handling and retry logic for API failures
- Monitor concurrent request limits to avoid rate limiting

### Data Validation
- Validate JSON output format before adding to dataset
- Check for empty or malformed responses
- Ensure balanced coverage across different documentation types

## Troubleshooting

### Common Issues
- **API Connection Errors**: Check endpoint URL and SGLang service status
- **Memory Errors**: Reduce `max_concurrent` and `batch_size` parameters  
- **Empty Responses**: Lower `max_tokens` or adjust `temperature`
- **JSON Parse Errors**: Review system prompt formatting requirements

### Monitoring
- Check `dataset_stats.json` for generation statistics
- Monitor log output for processing rates and error patterns
- Validate sample quality manually on small batches before full generation