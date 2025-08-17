# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an integrated dataset generation system for creating high-quality Unsloth-compatible datasets from Syncfusion WinForms documentation. The system processes Markdown files, integrates with Qdrant vector database, generates conversations using OpenAI API, transforms data into multiple formats (ShareGPT, Alpaca, OpenAI), and validates quality.

## Commands to Run Common Tasks

### Main Execution Commands
```bash
# Full pipeline execution
python main.py

# With custom configuration
python main.py --config custom_config.yaml

# Test mode with small sample size
python main.py --test-mode --sample-size 10

# Specific pipeline steps only
python main.py --steps md_processing,conversation_generation

# CLI interface (alternative)
python -m cli generate --test-mode --sample-size 10
```

### Testing Commands
```bash
# Run all tests
python run_tests.py

# Specific test types
python run_tests.py --unit-tests --integration-tests

# Individual test files (pytest pattern)
python -m pytest test_unsloth_dataset.py -v
python -m pytest test_openai_connector.py -v
python -m pytest test_quality_validator.py -v
```

### Configuration and Validation
```bash
# Validate configuration file
python -m cli validate-config --config config.yaml

# Create default configuration
python -m cli create-config new_config.yaml

# List available pipeline steps
python -m cli list-steps

# List output formats
python -m cli list-formats
```

### Component Analysis
```bash
# List supported Syncfusion components
python -m cli list-components

# Analyze existing dataset component distribution
python -m cli analyze-components output/dataset.jsonl
```

## High-Level Architecture

### Core Pipeline Flow
1. **MD Processing** (`md_processor/`) - Scans and processes Markdown files from documentation
2. **Qdrant Search** (`qdrant_connector/`) - Searches vector database for relevant context
3. **Conversation Generation** (`openai_connector/`) - Uses OpenAI API to generate training conversations
4. **Dataset Formatting** (`unsloth_dataset/`) - Transforms data into Unsloth-compatible formats
5. **Quality Validation** (`quality_validator/`) - Validates and filters generated content

### Module Architecture

#### Main Orchestration
- `main.py` - Primary pipeline orchestrator with async execution
- `cli/main.py` - Rich CLI interface with Click framework
- `config.yaml` - Central configuration for all components

#### Data Processing Modules
- `md_processor/` - MD file scanning, parsing, and preprocessing
  - `scanner.py` - File discovery and metadata extraction  
  - `parser.py` - Markdown parsing and content extraction
  - `processor.py` - Main processing logic and batch operations

- `openai_connector/` - OpenAI API integration and conversation generation
  - `client.py` - HTTP client with retry logic and rate limiting
  - `conversation_generator.py` - Conversation generation strategies
  - `prompt_engine.py` - Prompt templates and optimization

- `qdrant_connector/` - Vector database integration  
  - `client.py` - Qdrant client wrapper
  - `searcher.py` - Semantic search operations
  - `integration.py` - Local document processing integration

#### Output and Quality
- `unsloth_dataset/` - Multi-format dataset generation
  - `generator.py` - Main dataset generator
  - `formatters/` - Format-specific transformers (ShareGPT, Alpaca, OpenAI)
  - `component_organizer.py` - Syncfusion component categorization
  - `validator.py` - Unsloth compatibility validation

- `quality_validator/` - Content quality assurance
  - `quality_scorer.py` - Quality metrics calculation
  - `safety_filter.py` - Content safety validation
  - `duplicate_remover.py` - Deduplication logic
  - `auto_corrector.py` - Automatic quality improvement

#### Infrastructure
- `async_pipeline/` - Asynchronous pipeline management
  - `orchestrator.py` - Pipeline step coordination
  - `memory_manager.py` - Memory usage optimization
  - `progress_tracker.py` - Progress monitoring

- `logging_system/` - Structured logging and monitoring
  - `structured_logger.py` - JSON-structured logging
  - `metrics_collector.py` - Performance metrics
  - `health_checker.py` - System health monitoring

### Key Configuration Points

The system uses a centralized YAML configuration (`config.yaml`) that controls:
- OpenAI API settings (endpoint, model, token limits)
- Qdrant connection details (host, port, collection)  
- Dataset generation parameters (target count, formats, quality thresholds)
- Processing behavior (batch sizes, concurrency limits)

### Pipeline Step Dependencies

Steps must run in order due to data dependencies:
1. `md_processing` → produces document corpus
2. `qdrant_search` → enhances with vector search (optional)
3. `conversation_generation` → requires documents from step 1/2
4. `dataset_formatting` → requires conversations from step 3
5. `quality_validation` → validates final datasets from step 4

### Testing Strategy

The codebase uses a comprehensive testing approach:
- **Unit Tests**: Individual module testing (each `test_*.py` file)
- **Integration Tests**: Cross-module pipeline testing (`run_tests.py`)
- **Performance Tests**: Memory and speed benchmarking
- **Quality Tests**: Output validation and format compliance

Run `python run_tests.py` for full test suite with performance metrics and detailed reporting.

### Data Staging Areas

- `md_staging/` - Processed Markdown files organized by component
- `output/` - Generated datasets and reports
- `enhanced_unsloth_output/` - Enhanced dataset versions with additional metadata

### Memory and Performance Considerations

- Async pipeline design for I/O-bound operations
- Configurable batch sizes to manage memory usage
- Progress tracking and memory monitoring built-in
- Test mode available for development with small sample sizes

The system is designed to handle large-scale document processing while maintaining quality and performance through modular architecture and comprehensive monitoring.