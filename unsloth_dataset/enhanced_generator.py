#!/usr/bin/env python3
"""
Unsloth 채팅 템플릿 통합 개선된 데이터셋 생성기
"""

import asyncio
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass, asdict

from .chat_templates import (
    UnslothChatTemplateManager,
    ChatTemplateType,
    ChatTemplateConfig,
    create_chat_template_manager
)
from .generator import UnslothDatasetGenerator, DatasetConfig
from .formatters.sharegpt_formatter import ShareGPTFormatter
from .formatters.alpaca_formatter import AlpacaFormatter
from .formatters.openai_formatter import OpenAIFormatter

logger = logging.getLogger(__name__)


@dataclass
class EnhancedDatasetConfig:
    """개선된 데이터셋 생성 설정"""
    # 기본 설정
    target_count: int = 1000
    formats: List[str] = None
    output_dir: str = "output"
    
    # 채팅 템플릿 설정
    chat_templates: Dict[str, ChatTemplateConfig] = None
    enable_template_mapping: bool = True
    
    # 품질 설정
    min_tokens: int = 50
    max_tokens: int = 8192
    quality_threshold: float = 0.7
    remove_duplicates: bool = True
    
    # 훈련 설정
    train_split: float = 0.8
    add_generation_prompt: bool = False
    include_system_message: bool = True
    
    # 메타데이터 설정
    include_metadata: bool = True
    include_token_counts: bool = True
    include_template_info: bool = True
    
    def __post_init__(self):
        if self.formats is None:
            self.formats = ["sharegpt", "alpaca", "openai"]
        
        if self.chat_templates is None:
            self.chat_templates = {
                "sharegpt": ChatTemplateConfig(
                    template_type=ChatTemplateType.CHATML,
                    mapping={"role": "from", "content": "value", "user": "human", "assistant": "gpt"}
                ),
                "alpaca": ChatTemplateConfig(
                    template_type=ChatTemplateType.ALPACA
                ),
                "openai": ChatTemplateConfig(
                    template_type=ChatTemplateType.OPENAI
                )
            }


class EnhancedUnslothDatasetGenerator:
    """Unsloth 채팅 템플릿 통합 개선된 데이터셋 생성기"""
    
    def __init__(self, config: EnhancedDatasetConfig):
        self.config = config
        self.chat_template_manager = create_chat_template_manager()
        self.formatters = self._initialize_formatters()
        self.stats = {
            "total_processed": 0,
            "successful_conversions": 0,
            "failed_conversions": 0,
            "template_applications": {},
            "format_counts": {}
        }
    
    def _initialize_formatters(self) -> Dict[str, Any]:
        """포맷터들 초기화"""
        return {
            "sharegpt": ShareGPTFormatter(),
            "alpaca": AlpacaFormatter(),
            "openai": OpenAIFormatter()
        }
    
    async def generate_enhanced_datasets(
        self,
        conversations: List[Dict[str, Any]],
        output_prefix: str = "enhanced_dataset"
    ) -> Dict[str, Any]:
        """
        개선된 데이터셋 생성
        
        Args:
            conversations: 원본 대화 데이터
            output_prefix: 출력 파일 접두사
            
        Returns:
            생성 결과 딕셔너리
        """
        logger.info(f"개선된 데이터셋 생성 시작: {len(conversations)}개 대화")
        
        results = {
            "datasets": {},
            "template_formatted": {},
            "statistics": {},
            "files": {}
        }
        
        # 각 포맷별로 데이터셋 생성
        for format_name in self.config.formats:
            logger.info(f"{format_name} 포맷 데이터셋 생성 중...")
            
            try:
                # 1. 기본 포맷 변환
                formatted_data = await self._format_conversations(conversations, format_name)
                
                # 2. 채팅 템플릿 적용 (옵션)
                if self.config.enable_template_mapping and format_name in self.config.chat_templates:
                    template_formatted = await self._apply_chat_templates(
                        formatted_data, format_name
                    )
                    results["template_formatted"][format_name] = template_formatted
                
                # 3. 품질 검증 및 필터링
                validated_data = await self._validate_and_filter(formatted_data, format_name)
                
                # 4. 훈련/검증 분할
                train_data, val_data = self._split_dataset(validated_data)
                
                results["datasets"][format_name] = {
                    "train": train_data,
                    "validation": val_data,
                    "total": len(validated_data)
                }
                
                # 5. 파일 저장
                files = await self._save_datasets(
                    train_data, val_data, format_name, output_prefix
                )
                results["files"][format_name] = files
                
                self.stats["format_counts"][format_name] = len(validated_data)
                logger.info(f"{format_name} 포맷 완료: {len(validated_data)}개 대화")
                
            except Exception as e:
                logger.error(f"{format_name} 포맷 생성 실패: {e}")
                self.stats["failed_conversions"] += 1
        
        # 통계 정보 생성
        results["statistics"] = self._generate_statistics()
        
        # 종합 리포트 저장
        await self._save_comprehensive_report(results, output_prefix)
        
        logger.info("개선된 데이터셋 생성 완료")
        return results
    
    async def _format_conversations(
        self,
        conversations: List[Dict[str, Any]],
        format_name: str
    ) -> List[Dict[str, Any]]:
        """대화를 특정 포맷으로 변환"""
        if format_name not in self.formatters:
            raise ValueError(f"지원되지 않는 포맷: {format_name}")
        
        formatter = self.formatters[format_name]
        
        try:
            formatted_data = formatter.format(conversations, include_metadata=True)
            self.stats["successful_conversions"] += len(formatted_data)
            return formatted_data
        except Exception as e:
            logger.error(f"{format_name} 포맷 변환 실패: {e}")
            self.stats["failed_conversions"] += len(conversations)
            return []
    
    async def _apply_chat_templates(
        self,
        formatted_data: List[Dict[str, Any]],
        format_name: str
    ) -> List[Dict[str, Any]]:
        """채팅 템플릿 적용"""
        if format_name not in self.config.chat_templates:
            return formatted_data
        
        template_config = self.config.chat_templates[format_name]
        template_results = []
        
        for item in formatted_data:
            try:
                # 대화 데이터 추출
                if "conversations" in item:
                    conversations = item["conversations"]
                elif "messages" in item:
                    conversations = item["messages"]
                else:
                    # Alpaca 형식을 대화로 변환
                    conversations = []
                    if "instruction" in item:
                        conversations.append({"role": "user", "content": item["instruction"]})
                    if "output" in item:
                        conversations.append({"role": "assistant", "content": item["output"]})
                
                # 템플릿 적용
                formatted_text = self.chat_template_manager.apply_chat_template(
                    conversations=conversations,
                    template_type=template_config.template_type,
                    mapping=template_config.mapping,
                    add_generation_prompt=template_config.add_generation_prompt
                )
                
                # 결과 구성
                template_item = {
                    "text": formatted_text,
                    "template_type": template_config.template_type.value if isinstance(template_config.template_type, ChatTemplateType) else template_config.template_type,
                    "original_format": format_name,
                    **item.get("metadata", {})
                }
                
                if self.config.include_token_counts:
                    template_item["token_count"] = len(formatted_text.split())
                
                template_results.append(template_item)
                
                # 통계 업데이트
                template_type_str = template_config.template_type.value if isinstance(template_config.template_type, ChatTemplateType) else template_config.template_type
                if template_type_str not in self.stats["template_applications"]:
                    self.stats["template_applications"][template_type_str] = 0
                self.stats["template_applications"][template_type_str] += 1
                
            except Exception as e:
                logger.warning(f"템플릿 적용 실패: {e}")
                continue
        
        return template_results
    
    async def _validate_and_filter(
        self,
        data: List[Dict[str, Any]],
        format_name: str
    ) -> List[Dict[str, Any]]:
        """데이터 품질 검증 및 필터링"""
        validated_data = []
        
        for item in data:
            try:
                # 토큰 수 검증
                if "text" in item:
                    token_count = len(item["text"].split())
                elif "conversations" in item:
                    token_count = sum(len(conv.get("value", conv.get("content", "")).split()) 
                                    for conv in item["conversations"])
                else:
                    token_count = 0
                
                if token_count < self.config.min_tokens or token_count > self.config.max_tokens:
                    continue
                
                # 품질 점수 검증
                quality_score = item.get("metadata", {}).get("quality_score", 1.0)
                if quality_score < self.config.quality_threshold:
                    continue
                
                # 메타데이터 추가
                if self.config.include_metadata:
                    if "metadata" not in item:
                        item["metadata"] = {}
                    
                    item["metadata"].update({
                        "token_count": token_count,
                        "format": format_name,
                        "validated_at": datetime.now().isoformat(),
                        "quality_passed": True
                    })
                
                validated_data.append(item)
                
            except Exception as e:
                logger.warning(f"데이터 검증 실패: {e}")
                continue
        
        return validated_data
    
    def _split_dataset(
        self,
        data: List[Dict[str, Any]]
    ) -> tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """데이터셋을 훈련/검증으로 분할"""
        if not data:
            return [], []
        
        split_idx = int(len(data) * self.config.train_split)
        train_data = data[:split_idx]
        val_data = data[split_idx:]
        
        return train_data, val_data
    
    async def _save_datasets(
        self,
        train_data: List[Dict[str, Any]],
        val_data: List[Dict[str, Any]],
        format_name: str,
        output_prefix: str
    ) -> Dict[str, str]:
        """데이터셋 파일 저장"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = Path(self.config.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        files = {}
        
        # 훈련 데이터 저장
        if train_data:
            train_file = output_dir / f"{output_prefix}_{format_name}_train_{timestamp}.jsonl"
            with open(train_file, 'w', encoding='utf-8') as f:
                for item in train_data:
                    json.dump(item, f, ensure_ascii=False)
                    f.write('\n')
            files["train"] = str(train_file)
        
        # 검증 데이터 저장
        if val_data:
            val_file = output_dir / f"{output_prefix}_{format_name}_val_{timestamp}.jsonl"
            with open(val_file, 'w', encoding='utf-8') as f:
                for item in val_data:
                    json.dump(item, f, ensure_ascii=False)
                    f.write('\n')
            files["validation"] = str(val_file)
        
        # 전체 데이터 저장
        all_data = train_data + val_data
        if all_data:
            all_file = output_dir / f"{output_prefix}_{format_name}_all_{timestamp}.jsonl"
            with open(all_file, 'w', encoding='utf-8') as f:
                for item in all_data:
                    json.dump(item, f, ensure_ascii=False)
                    f.write('\n')
            files["all"] = str(all_file)
        
        return files
    
    def _generate_statistics(self) -> Dict[str, Any]:
        """통계 정보 생성"""
        total_generated = sum(self.stats["format_counts"].values())
        
        return {
            "generation_summary": {
                "total_input_conversations": self.stats["total_processed"],
                "total_generated_items": total_generated,
                "successful_conversions": self.stats["successful_conversions"],
                "failed_conversions": self.stats["failed_conversions"],
                "success_rate": self.stats["successful_conversions"] / max(1, self.stats["total_processed"])
            },
            "format_breakdown": self.stats["format_counts"],
            "template_applications": self.stats["template_applications"],
            "quality_metrics": {
                "min_tokens": self.config.min_tokens,
                "max_tokens": self.config.max_tokens,
                "quality_threshold": self.config.quality_threshold,
                "train_split": self.config.train_split
            },
            "configuration": {
                "formats": self.config.formats,
                "enable_template_mapping": self.config.enable_template_mapping,
                "include_metadata": self.config.include_metadata,
                "remove_duplicates": self.config.remove_duplicates
            }
        }
    
    async def _save_comprehensive_report(
        self,
        results: Dict[str, Any],
        output_prefix: str
    ) -> str:
        """종합 리포트 저장"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = Path(self.config.output_dir)
        report_file = output_dir / f"{output_prefix}_comprehensive_report_{timestamp}.json"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        logger.info(f"종합 리포트 저장: {report_file}")
        return str(report_file)


def create_enhanced_generator(config: EnhancedDatasetConfig) -> EnhancedUnslothDatasetGenerator:
    """개선된 데이터셋 생성기 생성"""
    return EnhancedUnslothDatasetGenerator(config)


# 편의 함수들
async def generate_unsloth_compatible_datasets(
    conversations: List[Dict[str, Any]],
    output_dir: str = "enhanced_output",
    formats: List[str] = None,
    chat_templates: Dict[str, ChatTemplateConfig] = None,
    **kwargs
) -> Dict[str, Any]:
    """Unsloth 호환 데이터셋 생성 편의 함수"""
    
    config = EnhancedDatasetConfig(
        formats=formats or ["sharegpt", "alpaca", "openai"],
        output_dir=output_dir,
        chat_templates=chat_templates,
        **kwargs
    )
    
    generator = create_enhanced_generator(config)
    return await generator.generate_enhanced_datasets(conversations)


if __name__ == "__main__":
    # 테스트 코드
    async def test_enhanced_generator():
        # 테스트 데이터
        test_conversations = [
            {
                "instruction": "Syncfusion WinForms GridControl에서 셀 병합을 설정하는 방법을 설명해주세요.",
                "input": "",
                "output": "GridControl에서 셀 병합을 설정하려면 다음과 같이 하세요:\n\n1. GridStyleInfo 설정\n2. MergeCell 속성 구성\n3. OnDemandCalculation 모드 활성화",
                "response": "GridControl에서 셀 병합을 설정하려면 다음과 같이 하세요:\n\n1. GridStyleInfo 설정\n2. MergeCell 속성 구성\n3. OnDemandCalculation 모드 활성화",
                "metadata": {
                    "component": "GridControl",
                    "difficulty": "Intermediate"
                }
            }
        ]
        
        # 개선된 생성기로 데이터셋 생성
        results = await generate_unsloth_compatible_datasets(
            conversations=test_conversations,
            output_dir="test_enhanced_output",
            formats=["sharegpt", "alpaca"],
            target_count=1,
            enable_template_mapping=True
        )
        
        print("=== 개선된 데이터셋 생성 결과 ===")
        print(f"생성된 포맷: {list(results['datasets'].keys())}")
        print(f"템플릿 적용: {list(results['template_formatted'].keys())}")
        print(f"통계: {results['statistics']['generation_summary']}")
    
    asyncio.run(test_enhanced_generator())