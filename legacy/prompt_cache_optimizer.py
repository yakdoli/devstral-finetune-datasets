#!/usr/bin/env python3
"""
Prompt cache optimization for SGLang backend
Implements efficient prompt caching for repeated system prompts
"""

import json
import asyncio
import aiohttp
from typing import Dict, Any, Optional
from dataclasses import dataclass
import hashlib
import logging

logger = logging.getLogger(__name__)

@dataclass
class CachedPrompt:
    """Cached prompt with hash for efficient reuse"""
    content: str
    hash: str
    cache_id: Optional[str] = None

class SGLangPromptCache:
    """Prompt caching manager for SGLang backend"""
    
    def __init__(self, endpoint: str):
        self.endpoint = endpoint
        self.cache: Dict[str, CachedPrompt] = {}
        
    def get_prompt_hash(self, content: str) -> str:
        """Generate hash for prompt content"""
        return hashlib.sha256(content.encode()).hexdigest()[:16]
    
    async def cache_system_prompt(self, session: aiohttp.ClientSession, 
                                system_prompt: str) -> str:
        """Cache system prompt and return cache ID"""
        
        prompt_hash = self.get_prompt_hash(system_prompt)
        
        if prompt_hash in self.cache:
            return self.cache[prompt_hash].cache_id
        
        # For SGLang, we can implement prompt prefix caching
        # This is a simplified version - actual implementation would depend on SGLang API
        try:
            # Pre-fill system prompt to warm up the cache
            payload = {
                "model": "qwen2.5-vl-instruct",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": "cache_warmup"}
                ],
                "max_tokens": 1,
                "temperature": 0.0,
                "stream": False
            }
            
            async with session.post(
                f"{self.endpoint}/chat/completions",
                json=payload
            ) as response:
                if response.status == 200:
                    result = await response.json()
                    # In real SGLang, this would return a cache ID
                    cache_id = f"cache_{prompt_hash}"
                    
                    cached_prompt = CachedPrompt(
                        content=system_prompt,
                        hash=prompt_hash,
                        cache_id=cache_id
                    )
                    self.cache[prompt_hash] = cached_prompt
                    
                    logger.info(f"Cached system prompt: {cache_id}")
                    return cache_id
                    
        except Exception as e:
            logger.warning(f"Prompt caching failed: {e}")
            
        return None
    
    async def get_cached_completion(self, session: aiohttp.ClientSession,
                                  system_prompt: str, user_prompt: str,
                                  **kwargs) -> Optional[Dict[str, Any]]:
        """Get completion using cached system prompt"""
        
        cache_id = await self.cache_system_prompt(session, system_prompt)
        
        # Use standard API with cached prompt reference
        payload = {
            "model": kwargs.get("model", "qwen2.5-vl-instruct"),
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "max_tokens": kwargs.get("max_tokens", 32000),
            "temperature": kwargs.get("temperature", 0.3),
            "stream": False
        }
        
        # Add cache hint if available (SGLang specific)
        if cache_id:
            payload["cache_id"] = cache_id
        
        try:
            async with session.post(
                f"{self.endpoint}/chat/completions",
                json=payload
            ) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    logger.error(f"API error: {response.status}")
                    return None
                    
        except Exception as e:
            logger.error(f"Completion error: {e}")
            return None

class BatchProcessor:
    """Batch processor with prompt caching optimization"""
    
    def __init__(self, endpoint: str):
        self.endpoint = endpoint
        self.cache_manager = SGLangPromptCache(endpoint)
        
    async def process_batch_with_cache(self, session: aiohttp.ClientSession,
                                     system_prompt: str, 
                                     user_prompts: list,
                                     **kwargs) -> list:
        """Process batch of prompts with shared system prompt caching"""
        
        # Pre-cache system prompt
        await self.cache_manager.cache_system_prompt(session, system_prompt)
        
        # Process user prompts concurrently
        tasks = []
        for user_prompt in user_prompts:
            task = self.cache_manager.get_cached_completion(
                session, system_prompt, user_prompt, **kwargs
            )
            tasks.append(task)
        
        # Execute batch with concurrency control
        semaphore = asyncio.Semaphore(kwargs.get("max_concurrent", 8))
        
        async def limited_task(task):
            async with semaphore:
                return await task
        
        results = await asyncio.gather(*[limited_task(task) for task in tasks])
        return [r for r in results if r is not None]

# Integration with main dataset generator
class OptimizedDatasetGenerator:
    """Enhanced dataset generator with prompt caching"""
    
    def __init__(self, config):
        self.config = config
        self.batch_processor = BatchProcessor(config.endpoint)
    
    async def generate_batch_qa_pairs(self, session: aiohttp.ClientSession,
                                    contents: list, page_infos: list) -> list:
        """Generate Q&A pairs for batch of content with caching"""
        
        system_prompt = """You are an expert at creating high-quality training data for code assistant fine-tuning. 
Generate diverse question-answer pairs from the given Syncfusion WinForms documentation.

Create 3-5 Q&A pairs that cover:
1. Conceptual understanding (what is X, how does Y work)
2. Implementation guidance (how to implement/use feature)
3. Code examples and best practices
4. Troubleshooting and common issues
5. API reference and parameters

Format as JSON array:
[
  {
    "instruction": "How to implement basic Essential Calculate functionality in WinForms?",
    "input": "",
    "output": "To implement Essential Calculate in WinForms, you need to: [detailed step-by-step answer with code examples]"
  }
]

Focus on practical developer questions that would benefit from this documentation."""

        # Prepare user prompts
        user_prompts = []
        for content, page_info in zip(contents, page_infos):
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
            user_prompts.append(user_prompt)
        
        # Process batch with caching
        results = await self.batch_processor.process_batch_with_cache(
            session, system_prompt, user_prompts,
            model=self.config.model,
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature,
            max_concurrent=self.config.max_concurrent
        )
        
        return results