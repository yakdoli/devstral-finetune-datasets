# Requirements Document

## Introduction

이 프로젝트는 Syncfusion WinForms 문서를 기반으로 고품질의 Unsloth 훈련용 데이터셋을 생성하는 통합 솔루션입니다. MD 파일 처리부터 벡터 데이터베이스 연동, AI 기반 대화 생성, 다중 포맷 변환, 품질 검증까지의 전체 파이프라인을 자동화하여 LLM 미세조정에 최적화된 데이터셋을 제공합니다.

## Requirements

### Requirement 1

**User Story:** As a ML engineer, I want to automatically process Syncfusion WinForms MD documentation files, so that I can extract structured content for dataset generation.

#### Acceptance Criteria

1. WHEN MD files are provided in the md_staging directory THEN the system SHALL scan and parse all MD files recursively
2. WHEN parsing MD files THEN the system SHALL extract metadata including component names, page numbers, and content structure
3. WHEN processing MD content THEN the system SHALL clean and normalize text while preserving code examples and API signatures
4. IF MD files contain malformed content THEN the system SHALL log warnings and continue processing valid sections
5. WHEN processing is complete THEN the system SHALL generate structured JSON metadata for each processed file

### Requirement 2

**User Story:** As a data scientist, I want to leverage Qdrant vector database for semantic search and context retrieval, so that I can generate contextually relevant training conversations.

#### Acceptance Criteria

1. WHEN connecting to Qdrant THEN the system SHALL establish connection to 100.88.88.88:6333 with collection ws-7491d651ae044c78
2. WHEN searching for context THEN the system SHALL perform semantic similarity search using sentence transformers
3. WHEN retrieving documents THEN the system SHALL return relevant context with similarity scores above 0.7 threshold
4. IF Qdrant connection fails THEN the system SHALL retry up to 3 times with exponential backoff
5. WHEN context is retrieved THEN the system SHALL format it for conversation generation with proper metadata

### Requirement 3

**User Story:** As an AI researcher, I want to generate high-quality conversations using OpenAI-compatible API, so that I can create diverse training examples for LLM fine-tuning.

#### Acceptance Criteria

1. WHEN generating conversations THEN the system SHALL use qwen2.5-vl-instruct model via http://123.37.28.120:9997/v1 endpoint
2. WHEN creating prompts THEN the system SHALL include relevant context from Qdrant search results
3. WHEN generating responses THEN the system SHALL maintain conversation coherence and technical accuracy
4. IF API requests fail THEN the system SHALL implement retry logic with rate limiting
5. WHEN conversations are generated THEN the system SHALL validate response quality and filter inappropriate content

### Requirement 4

**User Story:** As a dataset curator, I want to convert generated conversations into multiple standard formats, so that I can use them with different training frameworks.

#### Acceptance Criteria

1. WHEN formatting datasets THEN the system SHALL support ShareGPT, Alpaca, and OpenAI conversation formats
2. WHEN converting to ShareGPT format THEN the system SHALL structure conversations with proper role assignments (human/gpt)
3. WHEN converting to Alpaca format THEN the system SHALL create instruction-input-output triplets
4. WHEN converting to OpenAI format THEN the system SHALL format as messages array with role and content fields
5. WHEN saving datasets THEN the system SHALL output JSONL files with UTF-8 encoding

### Requirement 5

**User Story:** As a quality assurance engineer, I want comprehensive quality validation and filtering, so that I can ensure dataset meets training standards.

#### Acceptance Criteria

1. WHEN validating quality THEN the system SHALL calculate quality scores using ROUGE, BERT-score, and custom metrics
2. WHEN detecting duplicates THEN the system SHALL remove conversations with similarity above 0.9 threshold
3. WHEN checking safety THEN the system SHALL filter out inappropriate, harmful, or biased content
4. IF quality scores are below 0.6 threshold THEN the system SHALL flag or remove low-quality samples
5. WHEN validation is complete THEN the system SHALL generate detailed quality reports with statistics

### Requirement 6

**User Story:** As a system administrator, I want efficient batch processing and resource management, so that I can handle large-scale dataset generation without system overload.

#### Acceptance Criteria

1. WHEN processing large datasets THEN the system SHALL implement batch processing with configurable batch sizes (16-100)
2. WHEN making API calls THEN the system SHALL limit concurrent requests to maximum 8 simultaneous connections
3. WHEN managing memory THEN the system SHALL respect maximum sequence length of 8192 tokens
4. IF system resources are constrained THEN the system SHALL implement backpressure and graceful degradation
5. WHEN processing is active THEN the system SHALL display real-time progress indicators and ETA

### Requirement 7

**User Story:** As a developer, I want comprehensive logging and monitoring capabilities, so that I can debug issues and track processing performance.

#### Acceptance Criteria

1. WHEN system runs THEN the system SHALL log all major operations with INFO, WARNING, and ERROR levels
2. WHEN errors occur THEN the system SHALL provide detailed error messages with context and stack traces
3. WHEN processing completes THEN the system SHALL generate summary statistics including processing time and success rates
4. IF verbose mode is enabled THEN the system SHALL output detailed debug information
5. WHEN logging THEN the system SHALL support both console output and file logging with rotation

### Requirement 8

**User Story:** As an end user, I want a user-friendly CLI interface, so that I can easily configure and run the dataset generation pipeline.

#### Acceptance Criteria

1. WHEN running the system THEN the system SHALL provide intuitive command-line interface with clear help documentation
2. WHEN configuring THEN the system SHALL support YAML configuration files with validation
3. WHEN executing THEN the system SHALL allow selective pipeline step execution (e.g., only MD processing or only conversation generation)
4. IF invalid parameters are provided THEN the system SHALL display helpful error messages and usage examples
5. WHEN in test mode THEN the system SHALL process only a small sample for quick validation

### Requirement 9

**User Story:** As a Unsloth framework user, I want perfect compatibility with Unsloth training requirements, so that I can directly use generated datasets for model fine-tuning.

#### Acceptance Criteria

1. WHEN generating datasets THEN the system SHALL ensure full compatibility with Unsloth framework requirements
2. WHEN formatting conversations THEN the system SHALL follow Unsloth's expected data structure and field naming
3. WHEN validating compatibility THEN the system SHALL run Unsloth-specific validation checks
4. IF compatibility issues are detected THEN the system SHALL automatically correct common formatting problems
5. WHEN datasets are ready THEN the system SHALL provide Unsloth-ready training and validation splits

### Requirement 10

**User Story:** As a Syncfusion developer, I want specialized handling of WinForms documentation, so that I can generate domain-specific training data with accurate technical content.

#### Acceptance Criteria

1. WHEN processing Syncfusion docs THEN the system SHALL recognize and preserve API signatures, code examples, and component hierarchies
2. WHEN extracting content THEN the system SHALL maintain relationships between components and their documentation
3. WHEN generating conversations THEN the system SHALL create contextually appropriate questions about WinForms development
4. IF technical content is complex THEN the system SHALL break it down into digestible conversation segments
5. WHEN organizing output THEN the system SHALL group datasets by component categories for targeted training