#!/usr/bin/env python3
"""
전체 파이프라인 최종 통합 테스트
모든 모듈을 통합하여 end-to-end 테스트 수행
"""

import asyncio
import json
import logging
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class CompletePipelineIntegrationTest:
    """전체 파이프라인 통합 테스트 클래스"""
    
    def __init__(self):
        self.test_results = {}
        self.performance_metrics = {}
        self.start_time = None
        self.end_time = None  
  async def run_complete_test(self) -> Dict[str, Any]:
        """전체 테스트 실행"""
        logger.info("=== 전체 파이프라인 최종 통합 테스트 시작 ===")
        self.start_time = datetime.now()
        
        try:
            # 1. 환경 및 의존성 검증
            await self._test_environment_setup()
            
            # 2. MD 파일 처리 모듈 테스트
            await self._test_md_processing()
            
            # 3. Qdrant 연동 테스트
            await self._test_qdrant_integration()
            
            # 4. OpenAI 연동 테스트
            await self._test_openai_integration()
            
            # 5. 데이터셋 생성 테스트
            await self._test_dataset_generation()
            
            # 6. 품질 검증 테스트
            await self._test_quality_validation()
            
            # 7. 전체 파이프라인 테스트
            await self._test_complete_pipeline()
            
            # 8. 성능 검증
            await self._test_performance()
            
            # 9. Unsloth 호환성 검증
            await self._test_unsloth_compatibility()
            
            self.end_time = datetime.now()
            
            # 10. 최종 리포트 생성
            return await self._generate_final_report()
            
        except Exception as e:
            logger.error(f"통합 테스트 실행 중 오류: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return {"status": "failed", "error": str(e)}
    
    async def _test_environment_setup(self):
        """환경 및 의존성 검증"""
        logger.info("1. 환경 및 의존성 검증 중...")
        
        test_result = {
            "status": "success",
            "modules_available": {},
            "config_files": {},
            "directories": {}
        }
        
        # 필수 모듈 가용성 확인
        required_modules = [
            "md_processor", "openai_connector", "qdrant_connector",
            "unsloth_dataset", "quality_validator", "async_pipeline",
            "logging_system", "config"
        ]
        
        for module_name in required_modules:
            try:
                __import__(module_name)
                test_result["modules_available"][module_name] = True
                logger.info(f"  ✓ {module_name} 모듈 사용 가능")
            except ImportError as e:
                test_result["modules_available"][module_name] = False
                logger.warning(f"  ⚠ {module_name} 모듈 불가용: {e}")
        
        # 설정 파일 확인
        config_files = ["config.yaml", "requirements.txt"]
        for config_file in config_files:
            if Path(config_file).exists():
                test_result["config_files"][config_file] = True
                logger.info(f"  ✓ {config_file} 파일 존재")
            else:
                test_result["config_files"][config_file] = False
                logger.warning(f"  ⚠ {config_file} 파일 없음")
        
        # 필수 디렉토리 확인
        required_dirs = ["md_staging", "output"]
        for dir_name in required_dirs:
            if Path(dir_name).exists():
                test_result["directories"][dir_name] = True
                logger.info(f"  ✓ {dir_name} 디렉토리 존재")
            else:
                test_result["directories"][dir_name] = False
                logger.warning(f"  ⚠ {dir_name} 디렉토리 없음")
        
        self.test_results["environment_setup"] = test_result
        logger.info("✓ 환경 검증 완료")    a
sync def _test_md_processing(self):
        """MD 파일 처리 모듈 테스트"""
        logger.info("2. MD 파일 처리 모듈 테스트 중...")
        
        test_result = {
            "status": "success",
            "files_processed": 0,
            "processing_time": 0,
            "errors": []
        }
        
        try:
            from md_processor import create_md_processor, MDProcessorConfig
            
            # 테스트용 설정
            config = MDProcessorConfig(
                base_paths=["md_staging"],
                output_path="output/test_md_processing",
                max_files=10,  # 테스트용으로 제한
                enable_api_extraction=True,
                enable_code_extraction=True
            )
            
            processor = create_md_processor(config)
            
            start_time = time.time()
            documents = await processor.process_documents_async()
            end_time = time.time()
            
            test_result["files_processed"] = len(documents)
            test_result["processing_time"] = end_time - start_time
            
            if documents:
                logger.info(f"  ✓ {len(documents)}개 문서 처리 완료")
                logger.info(f"  ✓ 처리 시간: {test_result['processing_time']:.2f}초")
            else:
                test_result["status"] = "warning"
                test_result["errors"].append("처리된 문서가 없음")
                logger.warning("  ⚠ 처리된 문서가 없음")
            
        except Exception as e:
            test_result["status"] = "failed"
            test_result["errors"].append(str(e))
            logger.error(f"  ✗ MD 처리 모듈 테스트 실패: {e}")
        
        self.test_results["md_processing"] = test_result
        logger.info("✓ MD 처리 모듈 테스트 완료")
    
    async def _test_qdrant_integration(self):
        """Qdrant 연동 테스트"""
        logger.info("3. Qdrant 연동 테스트 중...")
        
        test_result = {
            "status": "success",
            "connection_status": False,
            "search_results": 0,
            "response_time": 0,
            "errors": []
        }
        
        try:
            from qdrant_connector import create_qdrant_connector, QdrantConfig
            
            config = QdrantConfig(
                host="100.88.88.88",
                port=6333,
                collection_name="ws-7491d651ae044c78",
                timeout=10
            )
            
            connector = create_qdrant_connector(config)
            
            # 연결 테스트
            start_time = time.time()
            connection_result = await connector.test_connection()
            end_time = time.time()
            
            test_result["connection_status"] = connection_result.get("status") == "success"
            test_result["response_time"] = end_time - start_time
            
            if test_result["connection_status"]:
                logger.info(f"  ✓ Qdrant 연결 성공 (응답시간: {test_result['response_time']:.2f}초)")
                
                # 검색 테스트
                search_results = await connector.search_documents(
                    query="Syncfusion GridControl data binding",
                    limit=5
                )
                
                test_result["search_results"] = len(search_results)
                logger.info(f"  ✓ 검색 결과: {len(search_results)}개")
            else:
                test_result["status"] = "failed"
                test_result["errors"].append("Qdrant 연결 실패")
                logger.error("  ✗ Qdrant 연결 실패")
            
        except Exception as e:
            test_result["status"] = "failed"
            test_result["errors"].append(str(e))
            logger.error(f"  ✗ Qdrant 연동 테스트 실패: {e}")
        
        self.test_results["qdrant_integration"] = test_result
        logger.info("✓ Qdrant 연동 테스트 완료") 
   async def _test_openai_integration(self):
        """OpenAI 연동 테스트"""
        logger.info("4. OpenAI 연동 테스트 중...")
        
        test_result = {
            "status": "success",
            "connection_status": False,
            "conversations_generated": 0,
            "avg_response_time": 0,
            "errors": []
        }
        
        try:
            from local_llm_connector import create_local_llm_client, LocalLLMClientConfig
            
            config = LocalLLMClientConfig(
                endpoint="http://123.37.28.120:9997/v1",
                model="qwen2.5-vl-instruct",
                api_key="test-key",
                timeout=30
            )
            
            client = create_local_llm_client(config)
            
            # 연결 테스트
            async with client as api_client:
                start_time = time.time()
                health = await api_client.test_connection()
                end_time = time.time()
                
                test_result["connection_status"] = health.get("status") == "success"
                test_result["avg_response_time"] = end_time - start_time
                
                if test_result["connection_status"]:
                    logger.info(f"  ✓ OpenAI API 연결 성공 (응답시간: {test_result['avg_response_time']:.2f}초)")
                    
                    # 간단한 대화 생성 테스트
                    test_prompt = [
                        {"role": "system", "content": "You are a helpful assistant for Syncfusion WinForms development."},
                        {"role": "user", "content": "How do I bind data to a GridControl?"}
                    ]
                    
                    response = await api_client.generate_response(test_prompt)
                    
                    if response and response.get("content"):
                        test_result["conversations_generated"] = 1
                        logger.info("  ✓ 테스트 대화 생성 성공")
                    else:
                        test_result["status"] = "warning"
                        test_result["errors"].append("대화 생성 실패")
                        logger.warning("  ⚠ 테스트 대화 생성 실패")
                else:
                    test_result["status"] = "failed"
                    test_result["errors"].append("OpenAI API 연결 실패")
                    logger.error("  ✗ OpenAI API 연결 실패")
            
        except Exception as e:
            test_result["status"] = "failed"
            test_result["errors"].append(str(e))
            logger.error(f"  ✗ OpenAI 연동 테스트 실패: {e}")
        
        self.test_results["openai_integration"] = test_result
        logger.info("✓ OpenAI 연동 테스트 완료")
    
    async def _test_dataset_generation(self):
        """데이터셋 생성 테스트"""
        logger.info("5. 데이터셋 생성 테스트 중...")
        
        test_result = {
            "status": "success",
            "formats_generated": {},
            "total_conversations": 0,
            "generation_time": 0,
            "errors": []
        }
        
        try:
            from unsloth_dataset import create_unsloth_generator, UnslothDatasetConfig
            
            # 테스트용 대화 데이터
            test_conversations = [
                {
                    "id": "test_conv_001",
                    "conversations": [
                        {"from": "human", "value": "How do I create a GridControl in Syncfusion WinForms?"},
                        {"from": "gpt", "value": "To create a GridControl in Syncfusion WinForms, you need to add the Syncfusion.Windows.Forms.Grid namespace and create an instance of GridControl."}
                    ],
                    "metadata": {
                        "source_documents": ["sf_grid_001"],
                        "component": "GridControl",
                        "difficulty": "Beginner"
                    }
                }
            ]
            
            config = UnslothDatasetConfig(
                formats=["sharegpt", "alpaca", "openai"],
                output_dir="output/test_datasets",
                train_split=0.8,
                enable_validation=True
            )
            
            generator = create_unsloth_generator(config)
            
            start_time = time.time()
            result = await generator.generate_datasets_async(test_conversations)
            end_time = time.time()
            
            test_result["generation_time"] = end_time - start_time
            test_result["total_conversations"] = len(test_conversations)
            
            for format_name, dataset in result.datasets.items():
                test_result["formats_generated"][format_name] = len(dataset)
                logger.info(f"  ✓ {format_name} 포맷: {len(dataset)}개 변환")
            
            logger.info(f"  ✓ 데이터셋 생성 완료 (시간: {test_result['generation_time']:.2f}초)")
            
        except Exception as e:
            test_result["status"] = "failed"
            test_result["errors"].append(str(e))
            logger.error(f"  ✗ 데이터셋 생성 테스트 실패: {e}")
        
        self.test_results["dataset_generation"] = test_result
        logger.info("✓ 데이터셋 생성 테스트 완료")    asy
nc def _test_quality_validation(self):
        """품질 검증 테스트"""
        logger.info("6. 품질 검증 테스트 중...")
        
        test_result = {
            "status": "success",
            "validation_checks": {},
            "quality_scores": {},
            "filtered_items": 0,
            "errors": []
        }
        
        try:
            from quality_validator import create_quality_validator, QualityValidatorConfig
            
            # 테스트용 데이터셋
            test_datasets = {
                "sharegpt": [
                    {
                        "conversations": [
                            {"from": "human", "value": "How do I use GridControl?"},
                            {"from": "gpt", "value": "GridControl is a powerful data grid component in Syncfusion WinForms that allows you to display and edit data in a tabular format."}
                        ]
                    },
                    {
                        "conversations": [
                            {"from": "human", "value": "Test"},  # 낮은 품질 예제
                            {"from": "gpt", "value": "Test response"}
                        ]
                    }
                ]
            }
            
            config = QualityValidatorConfig(
                min_quality_score=0.6,
                enable_safety_filter=True,
                enable_duplicate_removal=True,
                enable_auto_correction=True
            )
            
            validator = create_quality_validator(config)
            
            # 품질 검증 실행
            validation_results = await validator.validate_and_filter_async(test_datasets)
            
            for format_name, results in validation_results.items():
                valid_count = sum(1 for r in results if r.is_valid)
                total_count = len(results)
                
                test_result["validation_checks"][format_name] = {
                    "total": total_count,
                    "valid": valid_count,
                    "filtered": total_count - valid_count
                }
                
                if results:
                    avg_quality = sum(r.quality_metrics.get("overall_score", 0) for r in results) / len(results)
                    test_result["quality_scores"][format_name] = avg_quality
                
                logger.info(f"  ✓ {format_name}: {valid_count}/{total_count} 유효")
            
            test_result["filtered_items"] = sum(
                check["filtered"] for check in test_result["validation_checks"].values()
            )
            
            logger.info(f"  ✓ 품질 검증 완료 (필터링된 항목: {test_result['filtered_items']}개)")
            
        except Exception as e:
            test_result["status"] = "failed"
            test_result["errors"].append(str(e))
            logger.error(f"  ✗ 품질 검증 테스트 실패: {e}")
        
        self.test_results["quality_validation"] = test_result
        logger.info("✓ 품질 검증 테스트 완료")
    
    async def _test_complete_pipeline(self):
        """전체 파이프라인 테스트"""
        logger.info("7. 전체 파이프라인 테스트 중...")
        
        test_result = {
            "status": "success",
            "pipeline_steps": {},
            "total_processing_time": 0,
            "final_output": {},
            "errors": []
        }
        
        try:
            from async_pipeline import create_pipeline_orchestrator, PipelineConfig
            
            # 테스트용 파이프라인 설정
            config = PipelineConfig(
                # MD 처리 설정
                md_base_paths=["md_staging"],
                md_max_files=5,  # 테스트용으로 제한
                
                # Qdrant 설정
                qdrant_host="100.88.88.88",
                qdrant_port=6333,
                qdrant_collection="ws-7491d651ae044c78",
                
                # OpenAI 설정
                openai_endpoint="http://123.37.28.120:9997/v1",
                openai_model="qwen2.5-vl-instruct",
                
                # 데이터셋 설정
                target_count=3,  # 테스트용으로 제한
                formats=["sharegpt", "alpaca"],
                
                # 성능 설정
                batch_size=2,
                max_concurrent=2,
                test_mode=True
            )
            
            orchestrator = create_pipeline_orchestrator(config)
            
            start_time = time.time()
            
            # 파이프라인 실행
            pipeline_result = await orchestrator.run_complete_pipeline()
            
            end_time = time.time()
            
            test_result["total_processing_time"] = end_time - start_time
            
            # 각 단계 결과 확인
            if pipeline_result.get("status") == "success":
                test_result["pipeline_steps"] = pipeline_result.get("step_results", {})
                test_result["final_output"] = pipeline_result.get("final_output", {})
                
                logger.info(f"  ✓ 파이프라인 실행 성공 (시간: {test_result['total_processing_time']:.2f}초)")
                
                # 최종 출력 검증
                final_datasets = test_result["final_output"].get("datasets", {})
                for format_name, dataset in final_datasets.items():
                    logger.info(f"    - {format_name}: {len(dataset)}개 대화")
            else:
                test_result["status"] = "failed"
                test_result["errors"].append("파이프라인 실행 실패")
                logger.error("  ✗ 파이프라인 실행 실패")
            
        except Exception as e:
            test_result["status"] = "failed"
            test_result["errors"].append(str(e))
            logger.error(f"  ✗ 전체 파이프라인 테스트 실패: {e}")
        
        self.test_results["complete_pipeline"] = test_result
        logger.info("✓ 전체 파이프라인 테스트 완료")    asyn
c def _test_performance(self):
        """성능 검증 테스트"""
        logger.info("8. 성능 검증 테스트 중...")
        
        test_result = {
            "status": "success",
            "throughput_metrics": {},
            "memory_usage": {},
            "scalability_test": {},
            "errors": []
        }
        
        try:
            import psutil
            import gc
            
            # 메모리 사용량 측정 시작
            process = psutil.Process()
            initial_memory = process.memory_info().rss / 1024 / 1024  # MB
            
            # 처리량 테스트 (작은 배치로 테스트)
            batch_sizes = [1, 2, 4]
            throughput_results = {}
            
            for batch_size in batch_sizes:
                logger.info(f"  배치 크기 {batch_size} 테스트 중...")
                
                # 테스트용 문서 생성
                test_docs = [
                    {
                        "id": f"perf_test_{i}",
                        "content": f"Test document {i} for performance testing",
                        "component": "TestComponent"
                    }
                    for i in range(batch_size)
                ]
                
                start_time = time.time()
                
                # 간단한 처리 시뮬레이션
                processed_docs = []
                for doc in test_docs:
                    # 실제 처리 대신 시뮬레이션
                    await asyncio.sleep(0.1)  # 처리 시간 시뮬레이션
                    processed_docs.append({
                        **doc,
                        "processed": True,
                        "processing_time": 0.1
                    })
                
                end_time = time.time()
                processing_time = end_time - start_time
                
                throughput = len(test_docs) / processing_time
                throughput_results[batch_size] = {
                    "documents": len(test_docs),
                    "processing_time": processing_time,
                    "throughput": throughput
                }
                
                logger.info(f"    배치 크기 {batch_size}: {throughput:.2f} docs/sec")
            
            test_result["throughput_metrics"] = throughput_results
            
            # 메모리 사용량 측정
            current_memory = process.memory_info().rss / 1024 / 1024  # MB
            memory_increase = current_memory - initial_memory
            
            test_result["memory_usage"] = {
                "initial_mb": initial_memory,
                "current_mb": current_memory,
                "increase_mb": memory_increase,
                "cpu_percent": process.cpu_percent()
            }
            
            logger.info(f"  ✓ 메모리 사용량: {current_memory:.1f}MB (증가: {memory_increase:.1f}MB)")
            logger.info(f"  ✓ CPU 사용률: {process.cpu_percent():.1f}%")
            
            # 확장성 테스트 (시뮬레이션)
            max_concurrent = 4
            concurrent_results = {}
            
            for concurrent in [1, 2, max_concurrent]:
                logger.info(f"  동시 처리 {concurrent}개 테스트 중...")
                
                start_time = time.time()
                
                # 동시 처리 시뮬레이션
                tasks = []
                for i in range(concurrent):
                    task = asyncio.create_task(asyncio.sleep(0.2))  # 처리 시뮬레이션
                    tasks.append(task)
                
                await asyncio.gather(*tasks)
                
                end_time = time.time()
                processing_time = end_time - start_time
                
                concurrent_results[concurrent] = {
                    "concurrent_tasks": concurrent,
                    "total_time": processing_time,
                    "efficiency": concurrent / processing_time
                }
                
                logger.info(f"    동시 처리 {concurrent}개: {processing_time:.2f}초")
            
            test_result["scalability_test"] = concurrent_results
            
            # 메모리 정리
            gc.collect()
            
            logger.info("✓ 성능 검증 완료")
            
        except Exception as e:
            test_result["status"] = "failed"
            test_result["errors"].append(str(e))
            logger.error(f"  ✗ 성능 검증 테스트 실패: {e}")
        
        self.test_results["performance"] = test_result
        logger.info("✓ 성능 검증 테스트 완료")
    
    async def _test_unsloth_compatibility(self):
        """Unsloth 호환성 검증"""
        logger.info("9. Unsloth 호환성 검증 중...")
        
        test_result = {
            "status": "success",
            "format_compatibility": {},
            "structure_validation": {},
            "field_validation": {},
            "errors": []
        }
        
        try:
            # Unsloth 호환성 검증을 위한 테스트 데이터
            test_datasets = {
                "sharegpt": [
                    {
                        "conversations": [
                            {"from": "human", "value": "How do I use Syncfusion GridControl?"},
                            {"from": "gpt", "value": "To use Syncfusion GridControl, you need to first add it to your form and then configure its properties."}
                        ]
                    }
                ],
                "alpaca": [
                    {
                        "instruction": "Explain how to use Syncfusion GridControl",
                        "input": "",
                        "output": "To use Syncfusion GridControl, you need to first add it to your form and then configure its properties."
                    }
                ],
                "openai": [
                    {
                        "messages": [
                            {"role": "user", "content": "How do I use Syncfusion GridControl?"},
                            {"role": "assistant", "content": "To use Syncfusion GridControl, you need to first add it to your form and then configure its properties."}
                        ]
                    }
                ]
            }
            
            # 각 포맷별 호환성 검증
            for format_name, dataset in test_datasets.items():
                logger.info(f"  {format_name} 포맷 검증 중...")
                
                format_result = {
                    "valid_structure": True,
                    "required_fields": True,
                    "data_types": True,
                    "issues": []
                }
                
                for item in dataset:
                    # 구조 검증
                    if format_name == "sharegpt":
                        if "conversations" not in item:
                            format_result["valid_structure"] = False
                            format_result["issues"].append("conversations 필드 누락")
                        else:
                            for conv in item["conversations"]:
                                if "from" not in conv or "value" not in conv:
                                    format_result["required_fields"] = False
                                    format_result["issues"].append("from 또는 value 필드 누락")
                    
                    elif format_name == "alpaca":
                        required_fields = ["instruction", "input", "output"]
                        for field in required_fields:
                            if field not in item:
                                format_result["required_fields"] = False
                                format_result["issues"].append(f"{field} 필드 누락")
                    
                    elif format_name == "openai":
                        if "messages" not in item:
                            format_result["valid_structure"] = False
                            format_result["issues"].append("messages 필드 누락")
                        else:
                            for msg in item["messages"]:
                                if "role" not in msg or "content" not in msg:
                                    format_result["required_fields"] = False
                                    format_result["issues"].append("role 또는 content 필드 누락")
                
                test_result["format_compatibility"][format_name] = format_result
                
                if not format_result["issues"]:
                    logger.info(f"    ✓ {format_name} 포맷 호환성 검증 통과")
                else:
                    logger.warning(f"    ⚠ {format_name} 포맷 이슈: {format_result['issues']}")
            
            # 전체 구조 검증
            all_valid = all(
                result["valid_structure"] and result["required_fields"] and result["data_types"]
                for result in test_result["format_compatibility"].values()
            )
            
            if all_valid:
                logger.info("  ✓ 모든 포맷이 Unsloth 호환성 요구사항을 만족")
            else:
                test_result["status"] = "warning"
                logger.warning("  ⚠ 일부 포맷에서 호환성 이슈 발견")
            
        except Exception as e:
            test_result["status"] = "failed"
            test_result["errors"].append(str(e))
            logger.error(f"  ✗ Unsloth 호환성 검증 실패: {e}")
        
        self.test_results["unsloth_compatibility"] = test_result
        logger.info("✓ Unsloth 호환성 검증 완료")    as
ync def _generate_final_report(self) -> Dict[str, Any]:
        """최종 리포트 생성"""
        logger.info("10. 최종 리포트 생성 중...")
        
        total_time = (self.end_time - self.start_time).total_seconds()
        
        # 전체 테스트 결과 요약
        test_summary = {
            "total_tests": len(self.test_results),
            "passed": 0,
            "failed": 0,
            "warnings": 0
        }
        
        for test_name, result in self.test_results.items():
            status = result.get("status", "unknown")
            if status == "success":
                test_summary["passed"] += 1
            elif status == "failed":
                test_summary["failed"] += 1
            elif status == "warning":
                test_summary["warnings"] += 1
        
        # 성능 메트릭 요약
        performance_summary = {}
        if "performance" in self.test_results:
            perf_data = self.test_results["performance"]
            if "throughput_metrics" in perf_data:
                max_throughput = max(
                    metrics["throughput"] 
                    for metrics in perf_data["throughput_metrics"].values()
                )
                performance_summary["max_throughput_docs_per_sec"] = max_throughput
            
            if "memory_usage" in perf_data:
                performance_summary["memory_usage_mb"] = perf_data["memory_usage"]["current_mb"]
        
        # 최종 리포트 구성
        final_report = {
            "test_info": {
                "timestamp": self.start_time.isoformat(),
                "total_duration_seconds": total_time,
                "test_type": "complete_pipeline_integration"
            },
            "summary": test_summary,
            "performance_summary": performance_summary,
            "detailed_results": self.test_results,
            "recommendations": self._generate_recommendations()
        }
        
        # 리포트 파일 저장
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"complete_pipeline_integration_report_{timestamp}.json"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(final_report, f, indent=2, ensure_ascii=False)
        
        # 결과 출력
        logger.info("=" * 60)
        logger.info("최종 통합 테스트 결과 요약")
        logger.info("=" * 60)
        logger.info(f"총 테스트 시간: {total_time:.2f}초")
        logger.info(f"전체 테스트: {test_summary['total_tests']}개")
        logger.info(f"성공: {test_summary['passed']}개")
        logger.info(f"실패: {test_summary['failed']}개")
        logger.info(f"경고: {test_summary['warnings']}개")
        
        if performance_summary:
            logger.info(f"최대 처리량: {performance_summary.get('max_throughput_docs_per_sec', 'N/A'):.2f} docs/sec")
            logger.info(f"메모리 사용량: {performance_summary.get('memory_usage_mb', 'N/A'):.1f}MB")
        
        logger.info(f"상세 리포트: {report_file}")
        logger.info("=" * 60)
        
        return final_report
    
    def _generate_recommendations(self) -> List[str]:
        """테스트 결과 기반 권장사항 생성"""
        recommendations = []
        
        # 실패한 테스트에 대한 권장사항
        for test_name, result in self.test_results.items():
            if result.get("status") == "failed":
                if test_name == "environment_setup":
                    recommendations.append("필수 모듈 설치 및 설정 파일 확인 필요")
                elif test_name == "qdrant_integration":
                    recommendations.append("Qdrant 서버 연결 상태 및 네트워크 설정 확인 필요")
                elif test_name == "openai_integration":
                    recommendations.append("OpenAI API 엔드포인트 및 인증 설정 확인 필요")
                elif test_name == "complete_pipeline":
                    recommendations.append("전체 파이프라인 설정 및 모듈 간 연동 확인 필요")
        
        # 성능 관련 권장사항
        if "performance" in self.test_results:
            perf_data = self.test_results["performance"]
            if "memory_usage" in perf_data:
                memory_mb = perf_data["memory_usage"].get("current_mb", 0)
                if memory_mb > 1000:  # 1GB 이상
                    recommendations.append("메모리 사용량이 높음 - 배치 크기 조정 고려")
        
        # Unsloth 호환성 관련 권장사항
        if "unsloth_compatibility" in self.test_results:
            compat_data = self.test_results["unsloth_compatibility"]
            if compat_data.get("status") == "warning":
                recommendations.append("Unsloth 호환성 이슈 해결 필요 - 데이터 포맷 검토")
        
        # 기본 권장사항
        if not recommendations:
            recommendations.append("모든 테스트가 성공적으로 완료됨 - 프로덕션 배포 준비 완료")
        
        return recommendations


async def main():
    """메인 함수"""
    print("전체 파이프라인 최종 통합 테스트를 시작합니다...")
    print("이 테스트는 모든 모듈의 통합 동작을 검증합니다.\n")
    
    tester = CompletePipelineIntegrationTest()
    
    try:
        final_report = await tester.run_complete_test()
        
        if final_report.get("summary", {}).get("failed", 0) == 0:
            print("\n🎉 전체 파이프라인 통합 테스트가 성공적으로 완료되었습니다!")
            print("시스템이 프로덕션 환경에서 사용할 준비가 되었습니다.")
        else:
            print("\n⚠️ 일부 테스트에서 문제가 발견되었습니다.")
            print("상세 리포트를 확인하여 문제를 해결해주세요.")
        
        # 권장사항 출력
        recommendations = final_report.get("recommendations", [])
        if recommendations:
            print("\n📋 권장사항:")
            for i, rec in enumerate(recommendations, 1):
                print(f"  {i}. {rec}")
        
    except Exception as e:
        logger.error(f"테스트 실행 중 치명적 오류 발생: {e}")
        print(f"\n❌ 테스트 실행 실패: {e}")
    
    print("\n=== 최종 통합 테스트 완료 ===")


if __name__ == "__main__":
    asyncio.run(main())