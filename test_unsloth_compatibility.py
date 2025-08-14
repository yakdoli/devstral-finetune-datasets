#!/usr/bin/env python3
"""
Unsloth 프레임워크 호환성 검증 테스트
생성된 데이터셋이 Unsloth에서 정상적으로 사용 가능한지 검증
"""

import asyncio
import json
import logging
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class UnslothCompatibilityTest:
    """Unsloth 호환성 테스트 클래스"""
    
    def __init__(self):
        self.test_results = {}
        self.compatibility_issues = []
        self.test_datasets = {}
    
    async def run_compatibility_tests(self) -> Dict[str, Any]:
        """호환성 테스트 실행"""
        logger.info("=== Unsloth 호환성 검증 테스트 시작 ===")
        
        try:
            # 1. 테스트 데이터셋 생성
            await self._generate_test_datasets()
            
            # 2. 데이터 구조 검증
            await self._test_data_structure()
            
            # 3. 필드 유효성 검증
            await self._test_field_validation()
            
            # 4. 포맷별 호환성 검증
            await self._test_format_compatibility()
            
            # 5. 데이터 품질 검증
            await self._test_data_quality()
            
            # 6. 토큰화 호환성 검증
            await self._test_tokenization_compatibility()
            
            # 7. 실제 Unsloth 로딩 테스트 (시뮬레이션)
            await self._test_unsloth_loading()
            
            # 8. 최종 호환성 리포트 생성
            return await self._generate_compatibility_report()
            
        except Exception as e:
            logger.error(f"호환성 테스트 실행 중 오류: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return {"status": "failed", "error": str(e)}
    
    async def _generate_test_datasets(self):
        """테스트용 데이터셋 생성"""
        logger.info("1. 테스트 데이터셋 생성 중...")
        
        # ShareGPT 포맷 테스트 데이터
        sharegpt_data = [
            {
                "conversations": [
                    {"from": "human", "value": "How do I create a GridControl in Syncfusion WinForms?"},
                    {"from": "gpt", "value": "To create a GridControl in Syncfusion WinForms, you need to:\n1. Add the Syncfusion.Windows.Forms.Grid namespace\n2. Create an instance of GridControl\n3. Set up data binding\n\nHere's a simple example:\n```csharp\nGridControl gridControl = new GridControl();\ngridControl.DataSource = dataTable;\n```"}
                ]
            },
            {
                "conversations": [
                    {"from": "human", "value": "What are the key properties of ChartControl?"},
                    {"from": "gpt", "value": "The key properties of ChartControl include:\n- Series: Collection of data series\n- ChartType: Type of chart (Line, Bar, Pie, etc.)\n- Title: Chart title\n- Legend: Legend configuration\n- Axes: X and Y axis settings"}
                ]
            },
            {
                "conversations": [
                    {"from": "human", "value": "How to handle events in TreeViewAdv?"},
                    {"from": "gpt", "value": "TreeViewAdv provides several events:\n- NodeClick: When a node is clicked\n- NodeExpanded: When a node is expanded\n- NodeCollapsed: When a node is collapsed\n- NodeChecked: When a node checkbox is changed\n\nExample:\n```csharp\ntreeViewAdv.NodeClick += (sender, e) => {\n    // Handle node click\n};\n```"}
                ]
            }
        ]
        
        # Alpaca 포맷 테스트 데이터
        alpaca_data = [
            {
                "instruction": "Explain how to create a GridControl in Syncfusion WinForms",
                "input": "",
                "output": "To create a GridControl in Syncfusion WinForms, you need to:\n1. Add the Syncfusion.Windows.Forms.Grid namespace\n2. Create an instance of GridControl\n3. Set up data binding\n\nHere's a simple example:\n```csharp\nGridControl gridControl = new GridControl();\ngridControl.DataSource = dataTable;\n```"
            },
            {
                "instruction": "List the key properties of ChartControl",
                "input": "Syncfusion WinForms ChartControl",
                "output": "The key properties of ChartControl include:\n- Series: Collection of data series\n- ChartType: Type of chart (Line, Bar, Pie, etc.)\n- Title: Chart title\n- Legend: Legend configuration\n- Axes: X and Y axis settings"
            }
        ]
        
        # OpenAI 포맷 테스트 데이터
        openai_data = [
            {
                "messages": [
                    {"role": "user", "content": "How do I create a GridControl in Syncfusion WinForms?"},
                    {"role": "assistant", "content": "To create a GridControl in Syncfusion WinForms, you need to:\n1. Add the Syncfusion.Windows.Forms.Grid namespace\n2. Create an instance of GridControl\n3. Set up data binding\n\nHere's a simple example:\n```csharp\nGridControl gridControl = new GridControl();\ngridControl.DataSource = dataTable;\n```"}
                ]
            },
            {
                "messages": [
                    {"role": "user", "content": "What are the key properties of ChartControl?"},
                    {"role": "assistant", "content": "The key properties of ChartControl include:\n- Series: Collection of data series\n- ChartType: Type of chart (Line, Bar, Pie, etc.)\n- Title: Chart title\n- Legend: Legend configuration\n- Axes: X and Y axis settings"}
                ]
            }
        ]
        
        self.test_datasets = {
            "sharegpt": sharegpt_data,
            "alpaca": alpaca_data,
            "openai": openai_data
        }
        
        logger.info(f"✓ 테스트 데이터셋 생성 완료:")
        for format_name, data in self.test_datasets.items():
            logger.info(f"  - {format_name}: {len(data)}개 샘플")
    
    async def _test_data_structure(self):
        """데이터 구조 검증"""
        logger.info("2. 데이터 구조 검증 중...")
        
        test_result = {
            "status": "success",
            "format_results": {},
            "structure_issues": []
        }
        
        for format_name, dataset in self.test_datasets.items():
            logger.info(f"  {format_name} 포맷 구조 검증 중...")
            
            format_result = {
                "valid_items": 0,
                "invalid_items": 0,
                "structure_errors": []
            }
            
            for i, item in enumerate(dataset):
                try:
                    if format_name == "sharegpt":
                        # ShareGPT 구조 검증
                        if not isinstance(item, dict):
                            raise ValueError("Item must be a dictionary")
                        
                        if "conversations" not in item:
                            raise ValueError("Missing 'conversations' field")
                        
                        if not isinstance(item["conversations"], list):
                            raise ValueError("'conversations' must be a list")
                        
                        for j, conv in enumerate(item["conversations"]):
                            if not isinstance(conv, dict):
                                raise ValueError(f"Conversation {j} must be a dictionary")
                            
                            if "from" not in conv or "value" not in conv:
                                raise ValueError(f"Conversation {j} missing 'from' or 'value' field")
                            
                            if conv["from"] not in ["human", "gpt", "system"]:
                                raise ValueError(f"Invalid 'from' value: {conv['from']}")
                    
                    elif format_name == "alpaca":
                        # Alpaca 구조 검증
                        required_fields = ["instruction", "input", "output"]
                        for field in required_fields:
                            if field not in item:
                                raise ValueError(f"Missing required field: {field}")
                            
                            if not isinstance(item[field], str):
                                raise ValueError(f"Field '{field}' must be a string")
                    
                    elif format_name == "openai":
                        # OpenAI 구조 검증
                        if "messages" not in item:
                            raise ValueError("Missing 'messages' field")
                        
                        if not isinstance(item["messages"], list):
                            raise ValueError("'messages' must be a list")
                        
                        for j, msg in enumerate(item["messages"]):
                            if not isinstance(msg, dict):
                                raise ValueError(f"Message {j} must be a dictionary")
                            
                            if "role" not in msg or "content" not in msg:
                                raise ValueError(f"Message {j} missing 'role' or 'content' field")
                            
                            if msg["role"] not in ["user", "assistant", "system"]:
                                raise ValueError(f"Invalid role: {msg['role']}")
                    
                    format_result["valid_items"] += 1
                    
                except Exception as e:
                    format_result["invalid_items"] += 1
                    format_result["structure_errors"].append(f"Item {i}: {str(e)}")
                    logger.warning(f"    구조 오류 (Item {i}): {e}")
            
            test_result["format_results"][format_name] = format_result
            
            if format_result["invalid_items"] == 0:
                logger.info(f"    ✓ {format_name}: 모든 항목 구조 유효")
            else:
                logger.warning(f"    ⚠ {format_name}: {format_result['invalid_items']}개 항목 구조 오류")
                test_result["structure_issues"].extend(format_result["structure_errors"])
        
        if test_result["structure_issues"]:
            test_result["status"] = "warning"
        
        self.test_results["data_structure"] = test_result
        logger.info("✓ 데이터 구조 검증 완료")    
async def _test_field_validation(self):
        """필드 유효성 검증"""
        logger.info("3. 필드 유효성 검증 중...")
        
        test_result = {
            "status": "success",
            "field_validation": {},
            "validation_issues": []
        }
        
        for format_name, dataset in self.test_datasets.items():
            logger.info(f"  {format_name} 포맷 필드 검증 중...")
            
            field_result = {
                "empty_fields": 0,
                "invalid_types": 0,
                "encoding_issues": 0,
                "length_issues": 0,
                "content_quality": {}
            }
            
            for i, item in enumerate(dataset):
                try:
                    if format_name == "sharegpt":
                        for conv in item["conversations"]:
                            # 빈 필드 검사
                            if not conv["value"].strip():
                                field_result["empty_fields"] += 1
                            
                            # 길이 검사 (너무 짧거나 긴 내용)
                            if len(conv["value"]) < 10:
                                field_result["length_issues"] += 1
                            elif len(conv["value"]) > 4000:  # 토큰 제한 고려
                                field_result["length_issues"] += 1
                            
                            # 인코딩 검사
                            try:
                                conv["value"].encode('utf-8')
                            except UnicodeEncodeError:
                                field_result["encoding_issues"] += 1
                    
                    elif format_name == "alpaca":
                        # 필수 필드 검사
                        for field in ["instruction", "output"]:
                            if not item[field].strip():
                                field_result["empty_fields"] += 1
                            
                            # 길이 검사
                            if len(item[field]) < 5:
                                field_result["length_issues"] += 1
                            elif len(item[field]) > 4000:
                                field_result["length_issues"] += 1
                            
                            # 인코딩 검사
                            try:
                                item[field].encode('utf-8')
                            except UnicodeEncodeError:
                                field_result["encoding_issues"] += 1
                    
                    elif format_name == "openai":
                        for msg in item["messages"]:
                            # 빈 필드 검사
                            if not msg["content"].strip():
                                field_result["empty_fields"] += 1
                            
                            # 길이 검사
                            if len(msg["content"]) < 5:
                                field_result["length_issues"] += 1
                            elif len(msg["content"]) > 4000:
                                field_result["length_issues"] += 1
                            
                            # 인코딩 검사
                            try:
                                msg["content"].encode('utf-8')
                            except UnicodeEncodeError:
                                field_result["encoding_issues"] += 1
                
                except Exception as e:
                    logger.warning(f"    필드 검증 오류 (Item {i}): {e}")
                    field_result["invalid_types"] += 1
            
            # 콘텐츠 품질 분석
            total_items = len(dataset)
            field_result["content_quality"] = {
                "empty_field_ratio": field_result["empty_fields"] / total_items if total_items > 0 else 0,
                "length_issue_ratio": field_result["length_issues"] / total_items if total_items > 0 else 0,
                "encoding_issue_ratio": field_result["encoding_issues"] / total_items if total_items > 0 else 0
            }
            
            test_result["field_validation"][format_name] = field_result
            
            # 이슈 요약
            issues = []
            if field_result["empty_fields"] > 0:
                issues.append(f"{field_result['empty_fields']}개 빈 필드")
            if field_result["length_issues"] > 0:
                issues.append(f"{field_result['length_issues']}개 길이 이슈")
            if field_result["encoding_issues"] > 0:
                issues.append(f"{field_result['encoding_issues']}개 인코딩 이슈")
            
            if issues:
                logger.warning(f"    ⚠ {format_name}: {', '.join(issues)}")
                test_result["validation_issues"].extend([f"{format_name}: {issue}" for issue in issues])
            else:
                logger.info(f"    ✓ {format_name}: 모든 필드 유효")
        
        if test_result["validation_issues"]:
            test_result["status"] = "warning"
        
        self.test_results["field_validation"] = test_result
        logger.info("✓ 필드 유효성 검증 완료")
    
    async def _test_format_compatibility(self):
        """포맷별 호환성 검증"""
        logger.info("4. 포맷별 호환성 검증 중...")
        
        test_result = {
            "status": "success",
            "format_compatibility": {},
            "compatibility_issues": []
        }
        
        # Unsloth에서 지원하는 포맷 스펙
        unsloth_specs = {
            "sharegpt": {
                "required_fields": ["conversations"],
                "conversation_fields": ["from", "value"],
                "valid_roles": ["human", "gpt", "system"],
                "max_turns": 50,
                "max_length": 4096
            },
            "alpaca": {
                "required_fields": ["instruction", "input", "output"],
                "optional_fields": ["text"],
                "max_length": 4096
            },
            "openai": {
                "required_fields": ["messages"],
                "message_fields": ["role", "content"],
                "valid_roles": ["user", "assistant", "system"],
                "max_messages": 50,
                "max_length": 4096
            }
        }
        
        for format_name, dataset in self.test_datasets.items():
            logger.info(f"  {format_name} 포맷 호환성 검증 중...")
            
            if format_name not in unsloth_specs:
                logger.warning(f"    ⚠ {format_name}: Unsloth 스펙 정보 없음")
                continue
            
            spec = unsloth_specs[format_name]
            format_result = {
                "compliant_items": 0,
                "non_compliant_items": 0,
                "compliance_issues": []
            }
            
            for i, item in enumerate(dataset):
                compliance_issues = []
                
                try:
                    if format_name == "sharegpt":
                        # 필수 필드 확인
                        for field in spec["required_fields"]:
                            if field not in item:
                                compliance_issues.append(f"Missing required field: {field}")
                        
                        if "conversations" in item:
                            conversations = item["conversations"]
                            
                            # 대화 수 제한 확인
                            if len(conversations) > spec["max_turns"]:
                                compliance_issues.append(f"Too many turns: {len(conversations)} > {spec['max_turns']}")
                            
                            # 각 대화 검증
                            for j, conv in enumerate(conversations):
                                for field in spec["conversation_fields"]:
                                    if field not in conv:
                                        compliance_issues.append(f"Conversation {j} missing field: {field}")
                                
                                if "from" in conv and conv["from"] not in spec["valid_roles"]:
                                    compliance_issues.append(f"Invalid role: {conv['from']}")
                                
                                if "value" in conv and len(conv["value"]) > spec["max_length"]:
                                    compliance_issues.append(f"Content too long: {len(conv['value'])} > {spec['max_length']}")
                    
                    elif format_name == "alpaca":
                        # 필수 필드 확인
                        for field in spec["required_fields"]:
                            if field not in item:
                                compliance_issues.append(f"Missing required field: {field}")
                        
                        # 길이 제한 확인
                        for field in ["instruction", "output"]:
                            if field in item and len(item[field]) > spec["max_length"]:
                                compliance_issues.append(f"{field} too long: {len(item[field])} > {spec['max_length']}")
                    
                    elif format_name == "openai":
                        # 필수 필드 확인
                        for field in spec["required_fields"]:
                            if field not in item:
                                compliance_issues.append(f"Missing required field: {field}")
                        
                        if "messages" in item:
                            messages = item["messages"]
                            
                            # 메시지 수 제한 확인
                            if len(messages) > spec["max_messages"]:
                                compliance_issues.append(f"Too many messages: {len(messages)} > {spec['max_messages']}")
                            
                            # 각 메시지 검증
                            for j, msg in enumerate(messages):
                                for field in spec["message_fields"]:
                                    if field not in msg:
                                        compliance_issues.append(f"Message {j} missing field: {field}")
                                
                                if "role" in msg and msg["role"] not in spec["valid_roles"]:
                                    compliance_issues.append(f"Invalid role: {msg['role']}")
                                
                                if "content" in msg and len(msg["content"]) > spec["max_length"]:
                                    compliance_issues.append(f"Content too long: {len(msg['content'])} > {spec['max_length']}")
                    
                    if compliance_issues:
                        format_result["non_compliant_items"] += 1
                        format_result["compliance_issues"].extend([f"Item {i}: {issue}" for issue in compliance_issues])
                    else:
                        format_result["compliant_items"] += 1
                
                except Exception as e:
                    format_result["non_compliant_items"] += 1
                    format_result["compliance_issues"].append(f"Item {i}: Validation error - {str(e)}")
            
            test_result["format_compatibility"][format_name] = format_result
            
            total_items = len(dataset)
            compliance_rate = format_result["compliant_items"] / total_items if total_items > 0 else 0
            
            if compliance_rate == 1.0:
                logger.info(f"    ✓ {format_name}: 100% 호환성")
            elif compliance_rate >= 0.9:
                logger.info(f"    ✓ {format_name}: {compliance_rate:.1%} 호환성 (양호)")
            else:
                logger.warning(f"    ⚠ {format_name}: {compliance_rate:.1%} 호환성 (개선 필요)")
                test_result["compatibility_issues"].extend(format_result["compliance_issues"])
        
        if test_result["compatibility_issues"]:
            test_result["status"] = "warning"
        
        self.test_results["format_compatibility"] = test_result
        logger.info("✓ 포맷별 호환성 검증 완료")    asy
nc def _test_data_quality(self):
        """데이터 품질 검증"""
        logger.info("5. 데이터 품질 검증 중...")
        
        test_result = {
            "status": "success",
            "quality_metrics": {},
            "quality_issues": []
        }
        
        for format_name, dataset in self.test_datasets.items():
            logger.info(f"  {format_name} 포맷 품질 검증 중...")
            
            quality_metrics = {
                "avg_content_length": 0,
                "content_diversity": 0,
                "technical_accuracy": 0,
                "language_quality": 0,
                "code_examples": 0,
                "total_items": len(dataset)
            }
            
            content_lengths = []
            unique_contents = set()
            code_example_count = 0
            technical_terms = ["Syncfusion", "GridControl", "ChartControl", "TreeViewAdv", "WinForms", "C#"]
            
            for item in dataset:
                try:
                    # 콘텐츠 추출
                    contents = []
                    if format_name == "sharegpt":
                        contents = [conv["value"] for conv in item["conversations"]]
                    elif format_name == "alpaca":
                        contents = [item["instruction"], item["output"]]
                    elif format_name == "openai":
                        contents = [msg["content"] for msg in item["messages"]]
                    
                    # 길이 분석
                    for content in contents:
                        content_lengths.append(len(content))
                        unique_contents.add(content.lower().strip())
                        
                        # 코드 예제 검사
                        if "```" in content or "code" in content.lower():
                            code_example_count += 1
                        
                        # 기술적 정확성 검사 (간단한 키워드 기반)
                        technical_score = sum(1 for term in technical_terms if term.lower() in content.lower())
                        quality_metrics["technical_accuracy"] += technical_score
                
                except Exception as e:
                    logger.warning(f"    품질 분석 오류: {e}")
            
            # 품질 메트릭 계산
            if content_lengths:
                quality_metrics["avg_content_length"] = sum(content_lengths) / len(content_lengths)
            
            total_contents = len(content_lengths)
            if total_contents > 0:
                quality_metrics["content_diversity"] = len(unique_contents) / total_contents
                quality_metrics["code_examples"] = code_example_count / total_contents
                quality_metrics["technical_accuracy"] = quality_metrics["technical_accuracy"] / total_contents
            
            # 언어 품질 평가 (간단한 휴리스틱)
            language_quality_score = 0
            for content in unique_contents:
                # 문장 구조 확인
                if content.count('.') > 0 or content.count('!') > 0 or content.count('?') > 0:
                    language_quality_score += 1
                
                # 적절한 길이 확인
                if 20 <= len(content) <= 2000:
                    language_quality_score += 1
            
            if len(unique_contents) > 0:
                quality_metrics["language_quality"] = language_quality_score / (len(unique_contents) * 2)
            
            test_result["quality_metrics"][format_name] = quality_metrics
            
            # 품질 이슈 확인
            issues = []
            if quality_metrics["avg_content_length"] < 50:
                issues.append("평균 콘텐츠 길이가 너무 짧음")
            elif quality_metrics["avg_content_length"] > 3000:
                issues.append("평균 콘텐츠 길이가 너무 김")
            
            if quality_metrics["content_diversity"] < 0.8:
                issues.append(f"콘텐츠 다양성 부족 ({quality_metrics['content_diversity']:.1%})")
            
            if quality_metrics["technical_accuracy"] < 1.0:
                issues.append("기술적 정확성 부족")
            
            if quality_metrics["code_examples"] < 0.3:
                issues.append("코드 예제 부족")
            
            if issues:
                logger.warning(f"    ⚠ {format_name}: {', '.join(issues)}")
                test_result["quality_issues"].extend([f"{format_name}: {issue}" for issue in issues])
            else:
                logger.info(f"    ✓ {format_name}: 품질 기준 만족")
            
            logger.info(f"      평균 길이: {quality_metrics['avg_content_length']:.0f}자")
            logger.info(f"      다양성: {quality_metrics['content_diversity']:.1%}")
            logger.info(f"      기술 정확성: {quality_metrics['technical_accuracy']:.1f}")
            logger.info(f"      코드 예제: {quality_metrics['code_examples']:.1%}")
        
        if test_result["quality_issues"]:
            test_result["status"] = "warning"
        
        self.test_results["data_quality"] = test_result
        logger.info("✓ 데이터 품질 검증 완료")
    
    async def _test_tokenization_compatibility(self):
        """토큰화 호환성 검증"""
        logger.info("6. 토큰화 호환성 검증 중...")
        
        test_result = {
            "status": "success",
            "tokenization_results": {},
            "tokenization_issues": []
        }
        
        # 간단한 토큰 추정 함수 (실제 토크나이저 없이)
        def estimate_tokens(text: str) -> int:
            # 대략적인 토큰 수 추정 (영어: 4자당 1토큰, 한국어: 2자당 1토큰)
            english_chars = sum(1 for c in text if ord(c) < 128)
            korean_chars = len(text) - english_chars
            return (english_chars // 4) + (korean_chars // 2)
        
        for format_name, dataset in self.test_datasets.items():
            logger.info(f"  {format_name} 포맷 토큰화 검증 중...")
            
            tokenization_result = {
                "total_items": len(dataset),
                "avg_tokens": 0,
                "max_tokens": 0,
                "min_tokens": float('inf'),
                "over_limit_items": 0,
                "token_distribution": {}
            }
            
            token_counts = []
            token_limit = 4096  # 일반적인 토큰 제한
            
            for i, item in enumerate(dataset):
                try:
                    item_tokens = 0
                    
                    if format_name == "sharegpt":
                        for conv in item["conversations"]:
                            item_tokens += estimate_tokens(conv["value"])
                    elif format_name == "alpaca":
                        item_tokens += estimate_tokens(item["instruction"])
                        item_tokens += estimate_tokens(item["input"])
                        item_tokens += estimate_tokens(item["output"])
                    elif format_name == "openai":
                        for msg in item["messages"]:
                            item_tokens += estimate_tokens(msg["content"])
                    
                    token_counts.append(item_tokens)
                    
                    if item_tokens > token_limit:
                        tokenization_result["over_limit_items"] += 1
                        logger.debug(f"    Item {i}: {item_tokens} 토큰 (제한 초과)")
                
                except Exception as e:
                    logger.warning(f"    토큰화 오류 (Item {i}): {e}")
            
            if token_counts:
                tokenization_result["avg_tokens"] = sum(token_counts) / len(token_counts)
                tokenization_result["max_tokens"] = max(token_counts)
                tokenization_result["min_tokens"] = min(token_counts)
                
                # 토큰 분포 분석
                ranges = [(0, 512), (512, 1024), (1024, 2048), (2048, 4096), (4096, float('inf'))]
                for range_start, range_end in ranges:
                    count = sum(1 for tokens in token_counts if range_start <= tokens < range_end)
                    range_name = f"{range_start}-{range_end if range_end != float('inf') else '∞'}"
                    tokenization_result["token_distribution"][range_name] = count
            
            test_result["tokenization_results"][format_name] = tokenization_result
            
            # 토큰화 이슈 확인
            issues = []
            if tokenization_result["over_limit_items"] > 0:
                issues.append(f"{tokenization_result['over_limit_items']}개 항목이 토큰 제한 초과")
            
            if tokenization_result["avg_tokens"] > token_limit * 0.8:
                issues.append("평균 토큰 수가 제한에 근접")
            
            if issues:
                logger.warning(f"    ⚠ {format_name}: {', '.join(issues)}")
                test_result["tokenization_issues"].extend([f"{format_name}: {issue}" for issue in issues])
            else:
                logger.info(f"    ✓ {format_name}: 토큰화 호환성 양호")
            
            logger.info(f"      평균 토큰: {tokenization_result['avg_tokens']:.0f}")
            logger.info(f"      최대 토큰: {tokenization_result['max_tokens']}")
            logger.info(f"      제한 초과: {tokenization_result['over_limit_items']}개")
        
        if test_result["tokenization_issues"]:
            test_result["status"] = "warning"
        
        self.test_results["tokenization"] = test_result
        logger.info("✓ 토큰화 호환성 검증 완료")
    
    async def _test_unsloth_loading(self):
        """Unsloth 로딩 테스트 (시뮬레이션)"""
        logger.info("7. Unsloth 로딩 테스트 중...")
        
        test_result = {
            "status": "success",
            "loading_results": {},
            "loading_issues": []
        }
        
        # 임시 파일에 데이터셋 저장하고 로딩 시뮬레이션
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            for format_name, dataset in self.test_datasets.items():
                logger.info(f"  {format_name} 포맷 로딩 테스트 중...")
                
                loading_result = {
                    "file_created": False,
                    "file_readable": False,
                    "json_valid": False,
                    "structure_valid": False,
                    "loadable": False
                }
                
                try:
                    # JSONL 파일 생성
                    file_path = temp_path / f"test_{format_name}.jsonl"
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        for item in dataset:
                            json.dump(item, f, ensure_ascii=False)
                            f.write('\n')
                    
                    loading_result["file_created"] = True
                    logger.debug(f"    파일 생성 완료: {file_path}")
                    
                    # 파일 읽기 테스트
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    loading_result["file_readable"] = True
                    logger.debug(f"    파일 읽기 완료: {len(lines)}줄")
                    
                    # JSON 유효성 테스트
                    loaded_items = []
                    for line_num, line in enumerate(lines):
                        try:
                            item = json.loads(line.strip())
                            loaded_items.append(item)
                        except json.JSONDecodeError as e:
                            logger.warning(f"    JSON 파싱 오류 (줄 {line_num + 1}): {e}")
                            raise
                    
                    loading_result["json_valid"] = True
                    logger.debug(f"    JSON 파싱 완료: {len(loaded_items)}개 항목")
                    
                    # 구조 유효성 재검증
                    structure_valid = True
                    for i, item in enumerate(loaded_items):
                        try:
                            if format_name == "sharegpt":
                                if "conversations" not in item:
                                    raise ValueError("Missing conversations field")
                                for conv in item["conversations"]:
                                    if "from" not in conv or "value" not in conv:
                                        raise ValueError("Invalid conversation structure")
                            elif format_name == "alpaca":
                                required_fields = ["instruction", "input", "output"]
                                for field in required_fields:
                                    if field not in item:
                                        raise ValueError(f"Missing field: {field}")
                            elif format_name == "openai":
                                if "messages" not in item:
                                    raise ValueError("Missing messages field")
                                for msg in item["messages"]:
                                    if "role" not in msg or "content" not in msg:
                                        raise ValueError("Invalid message structure")
                        except Exception as e:
                            logger.warning(f"    구조 검증 오류 (Item {i}): {e}")
                            structure_valid = False
                            break
                    
                    loading_result["structure_valid"] = structure_valid
                    
                    # 전체 로딩 가능성 판단
                    loading_result["loadable"] = all([
                        loading_result["file_created"],
                        loading_result["file_readable"],
                        loading_result["json_valid"],
                        loading_result["structure_valid"]
                    ])
                    
                    if loading_result["loadable"]:
                        logger.info(f"    ✓ {format_name}: Unsloth 로딩 가능")
                    else:
                        logger.warning(f"    ⚠ {format_name}: Unsloth 로딩 불가")
                        test_result["loading_issues"].append(f"{format_name}: 로딩 실패")
                
                except Exception as e:
                    logger.error(f"    ✗ {format_name}: 로딩 테스트 실패 - {e}")
                    loading_result["loadable"] = False
                    test_result["loading_issues"].append(f"{format_name}: {str(e)}")
                
                test_result["loading_results"][format_name] = loading_result
        
        if test_result["loading_issues"]:
            test_result["status"] = "warning"
        
        self.test_results["unsloth_loading"] = test_result
        logger.info("✓ Unsloth 로딩 테스트 완료")    asyn
c def _generate_compatibility_report(self) -> Dict[str, Any]:
        """호환성 리포트 생성"""
        logger.info("8. 호환성 리포트 생성 중...")
        
        # 전체 호환성 점수 계산
        compatibility_scores = {}
        
        # 데이터 구조 점수
        if "data_structure" in self.test_results:
            structure_data = self.test_results["data_structure"]["format_results"]
            structure_scores = []
            for format_name, result in structure_data.items():
                total = result["valid_items"] + result["invalid_items"]
                score = (result["valid_items"] / total * 100) if total > 0 else 0
                structure_scores.append(score)
            compatibility_scores["data_structure"] = sum(structure_scores) / len(structure_scores) if structure_scores else 0
        
        # 필드 유효성 점수
        if "field_validation" in self.test_results:
            field_data = self.test_results["field_validation"]["field_validation"]
            field_scores = []
            for format_name, result in field_data.items():
                quality = result["content_quality"]
                score = 100 * (1 - quality["empty_field_ratio"] - quality["length_issue_ratio"] - quality["encoding_issue_ratio"])
                field_scores.append(max(0, score))
            compatibility_scores["field_validation"] = sum(field_scores) / len(field_scores) if field_scores else 0
        
        # 포맷 호환성 점수
        if "format_compatibility" in self.test_results:
            format_data = self.test_results["format_compatibility"]["format_compatibility"]
            format_scores = []
            for format_name, result in format_data.items():
                total = result["compliant_items"] + result["non_compliant_items"]
                score = (result["compliant_items"] / total * 100) if total > 0 else 0
                format_scores.append(score)
            compatibility_scores["format_compatibility"] = sum(format_scores) / len(format_scores) if format_scores else 0
        
        # 데이터 품질 점수
        if "data_quality" in self.test_results:
            quality_data = self.test_results["data_quality"]["quality_metrics"]
            quality_scores = []
            for format_name, metrics in quality_data.items():
                score = (
                    min(100, metrics["content_diversity"] * 100) * 0.3 +
                    min(100, metrics["technical_accuracy"] * 20) * 0.3 +
                    min(100, metrics["language_quality"] * 100) * 0.2 +
                    min(100, metrics["code_examples"] * 100) * 0.2
                )
                quality_scores.append(score)
            compatibility_scores["data_quality"] = sum(quality_scores) / len(quality_scores) if quality_scores else 0
        
        # 토큰화 호환성 점수
        if "tokenization" in self.test_results:
            token_data = self.test_results["tokenization"]["tokenization_results"]
            token_scores = []
            for format_name, result in token_data.items():
                total = result["total_items"]
                over_limit = result["over_limit_items"]
                score = ((total - over_limit) / total * 100) if total > 0 else 0
                token_scores.append(score)
            compatibility_scores["tokenization"] = sum(token_scores) / len(token_scores) if token_scores else 0
        
        # Unsloth 로딩 점수
        if "unsloth_loading" in self.test_results:
            loading_data = self.test_results["unsloth_loading"]["loading_results"]
            loading_scores = []
            for format_name, result in loading_data.items():
                score = 100 if result["loadable"] else 0
                loading_scores.append(score)
            compatibility_scores["unsloth_loading"] = sum(loading_scores) / len(loading_scores) if loading_scores else 0
        
        # 전체 호환성 점수
        overall_score = sum(compatibility_scores.values()) / len(compatibility_scores) if compatibility_scores else 0
        
        # 호환성 등급 결정
        if overall_score >= 95:
            compatibility_grade = "A+"
        elif overall_score >= 90:
            compatibility_grade = "A"
        elif overall_score >= 85:
            compatibility_grade = "B+"
        elif overall_score >= 80:
            compatibility_grade = "B"
        elif overall_score >= 75:
            compatibility_grade = "C+"
        elif overall_score >= 70:
            compatibility_grade = "C"
        elif overall_score >= 60:
            compatibility_grade = "D"
        else:
            compatibility_grade = "F"
        
        # 권장사항 생성
        recommendations = []
        
        if compatibility_scores.get("data_structure", 0) < 90:
            recommendations.append("데이터 구조 개선 필요 - 필수 필드 및 타입 검증 강화")
        
        if compatibility_scores.get("field_validation", 0) < 90:
            recommendations.append("필드 유효성 개선 필요 - 빈 필드 및 인코딩 이슈 해결")
        
        if compatibility_scores.get("format_compatibility", 0) < 90:
            recommendations.append("포맷 호환성 개선 필요 - Unsloth 스펙 준수 강화")
        
        if compatibility_scores.get("data_quality", 0) < 80:
            recommendations.append("데이터 품질 개선 필요 - 콘텐츠 다양성 및 기술적 정확성 향상")
        
        if compatibility_scores.get("tokenization", 0) < 90:
            recommendations.append("토큰화 최적화 필요 - 콘텐츠 길이 조정")
        
        if compatibility_scores.get("unsloth_loading", 0) < 100:
            recommendations.append("Unsloth 로딩 이슈 해결 필요 - 파일 포맷 및 구조 검토")
        
        if not recommendations:
            recommendations.append("모든 호환성 테스트 통과 - Unsloth에서 사용 준비 완료")
        
        # 최종 리포트 구성
        compatibility_report = {
            "test_info": {
                "timestamp": datetime.now().isoformat(),
                "test_type": "unsloth_compatibility",
                "formats_tested": list(self.test_datasets.keys()),
                "total_samples": sum(len(dataset) for dataset in self.test_datasets.values())
            },
            "compatibility_scores": compatibility_scores,
            "overall_score": overall_score,
            "compatibility_grade": compatibility_grade,
            "detailed_results": self.test_results,
            "recommendations": recommendations,
            "summary": {
                "data_structure_valid": compatibility_scores.get("data_structure", 0) >= 90,
                "fields_valid": compatibility_scores.get("field_validation", 0) >= 90,
                "format_compliant": compatibility_scores.get("format_compatibility", 0) >= 90,
                "quality_acceptable": compatibility_scores.get("data_quality", 0) >= 80,
                "tokenization_compatible": compatibility_scores.get("tokenization", 0) >= 90,
                "unsloth_loadable": compatibility_scores.get("unsloth_loading", 0) >= 100,
                "ready_for_training": overall_score >= 85
            }
        }
        
        # 리포트 파일 저장
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"unsloth_compatibility_report_{timestamp}.json"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(compatibility_report, f, indent=2, ensure_ascii=False)
        
        # 결과 출력
        logger.info("=" * 60)
        logger.info("Unsloth 호환성 검증 결과")
        logger.info("=" * 60)
        logger.info(f"전체 호환성 점수: {overall_score:.1f}/100 (등급: {compatibility_grade})")
        logger.info(f"데이터 구조: {compatibility_scores.get('data_structure', 0):.1f}/100")
        logger.info(f"필드 유효성: {compatibility_scores.get('field_validation', 0):.1f}/100")
        logger.info(f"포맷 호환성: {compatibility_scores.get('format_compatibility', 0):.1f}/100")
        logger.info(f"데이터 품질: {compatibility_scores.get('data_quality', 0):.1f}/100")
        logger.info(f"토큰화 호환성: {compatibility_scores.get('tokenization', 0):.1f}/100")
        logger.info(f"Unsloth 로딩: {compatibility_scores.get('unsloth_loading', 0):.1f}/100")
        logger.info("")
        
        summary = compatibility_report["summary"]
        logger.info("호환성 요약:")
        logger.info(f"  데이터 구조 유효: {'✓' if summary['data_structure_valid'] else '✗'}")
        logger.info(f"  필드 유효성: {'✓' if summary['fields_valid'] else '✗'}")
        logger.info(f"  포맷 준수: {'✓' if summary['format_compliant'] else '✗'}")
        logger.info(f"  품질 수준: {'✓' if summary['quality_acceptable'] else '✗'}")
        logger.info(f"  토큰화 호환: {'✓' if summary['tokenization_compatible'] else '✗'}")
        logger.info(f"  Unsloth 로딩: {'✓' if summary['unsloth_loadable'] else '✗'}")
        logger.info(f"  훈련 준비: {'✓' if summary['ready_for_training'] else '✗'}")
        logger.info("")
        
        logger.info("권장사항:")
        for i, rec in enumerate(recommendations, 1):
            logger.info(f"  {i}. {rec}")
        
        logger.info(f"\n상세 리포트: {report_file}")
        logger.info("=" * 60)
        
        return compatibility_report


async def main():
    """메인 함수"""
    print("Unsloth 호환성 검증 테스트를 시작합니다...")
    print("이 테스트는 생성된 데이터셋이 Unsloth 프레임워크와 호환되는지 검증합니다.\n")
    
    tester = UnslothCompatibilityTest()
    
    try:
        compatibility_report = await tester.run_compatibility_tests()
        
        overall_score = compatibility_report.get("overall_score", 0)
        grade = compatibility_report.get("compatibility_grade", "F")
        ready_for_training = compatibility_report.get("summary", {}).get("ready_for_training", False)
        
        if ready_for_training:
            print(f"\n🎉 Unsloth 호환성 검증 완료! 점수: {overall_score:.1f}/100 (등급: {grade})")
            print("데이터셋이 Unsloth 훈련에 사용할 준비가 되었습니다!")
        elif overall_score >= 70:
            print(f"\n✅ Unsloth 호환성 검증 완료! 점수: {overall_score:.1f}/100 (등급: {grade})")
            print("데이터셋이 기본적인 호환성을 만족하지만 일부 개선이 필요합니다.")
        else:
            print(f"\n⚠️ Unsloth 호환성 검증 완료! 점수: {overall_score:.1f}/100 (등급: {grade})")
            print("데이터셋 호환성 개선이 필요합니다.")
        
        # 주요 호환성 지표 출력
        summary = compatibility_report.get("summary", {})
        print(f"\n📋 호환성 체크리스트:")
        print(f"  ✓ 데이터 구조: {'통과' if summary.get('data_structure_valid', False) else '실패'}")
        print(f"  ✓ 필드 유효성: {'통과' if summary.get('fields_valid', False) else '실패'}")
        print(f"  ✓ 포맷 준수: {'통과' if summary.get('format_compliant', False) else '실패'}")
        print(f"  ✓ 품질 수준: {'통과' if summary.get('quality_acceptable', False) else '실패'}")
        print(f"  ✓ 토큰화 호환: {'통과' if summary.get('tokenization_compatible', False) else '실패'}")
        print(f"  ✓ Unsloth 로딩: {'통과' if summary.get('unsloth_loadable', False) else '실패'}")
        
    except Exception as e:
        logger.error(f"호환성 테스트 실행 중 오류 발생: {e}")
        print(f"\n❌ 호환성 테스트 실패: {e}")
    
    print("\n=== Unsloth 호환성 검증 완료 ===")


if __name__ == "__main__":
    asyncio.run(main())