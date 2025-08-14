#!/usr/bin/env python3
"""
간단한 통합 테스트
기본적인 모듈 로딩 및 기능 테스트
"""

import asyncio
import json
import logging
import sys
from datetime import datetime
from pathlib import Path

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def test_module_imports():
    """모듈 임포트 테스트"""
    logger.info("모듈 임포트 테스트 중...")
    
    test_results = {}
    
    # 필수 모듈들
    modules_to_test = [
        "md_processor",
        "openai_connector", 
        "qdrant_connector",
        "unsloth_dataset",
        "quality_validator",
        "async_pipeline",
        "logging_system",
        "config"
    ]
    
    for module_name in modules_to_test:
        try:
            __import__(module_name)
            test_results[module_name] = "success"
            logger.info(f"  ✓ {module_name} 모듈 로딩 성공")
        except ImportError as e:
            test_results[module_name] = f"failed: {e}"
            logger.warning(f"  ⚠ {module_name} 모듈 로딩 실패: {e}")
        except Exception as e:
            test_results[module_name] = f"error: {e}"
            logger.error(f"  ✗ {module_name} 모듈 오류: {e}")
    
    return test_results


async def test_file_structure():
    """파일 구조 테스트"""
    logger.info("파일 구조 테스트 중...")
    
    test_results = {}
    
    # 필수 파일들
    required_files = [
        "config.yaml",
        "requirements.txt",
        "main.py"
    ]
    
    # 필수 디렉토리들
    required_dirs = [
        "md_processor",
        "openai_connector",
        "qdrant_connector", 
        "unsloth_dataset",
        "quality_validator",
        "md_staging",
        "output"
    ]
    
    for file_path in required_files:
        if Path(file_path).exists():
            test_results[f"file_{file_path}"] = "exists"
            logger.info(f"  ✓ {file_path} 파일 존재")
        else:
            test_results[f"file_{file_path}"] = "missing"
            logger.warning(f"  ⚠ {file_path} 파일 없음")
    
    for dir_path in required_dirs:
        if Path(dir_path).exists():
            test_results[f"dir_{dir_path}"] = "exists"
            logger.info(f"  ✓ {dir_path} 디렉토리 존재")
        else:
            test_results[f"dir_{dir_path}"] = "missing"
            logger.warning(f"  ⚠ {dir_path} 디렉토리 없음")
    
    return test_results


async def test_basic_functionality():
    """기본 기능 테스트"""
    logger.info("기본 기능 테스트 중...")
    
    test_results = {}
    
    try:
        # MD 프로세서 기본 테스트
        try:
            from md_processor import create_md_processor, MDProcessorConfig
            config = MDProcessorConfig(base_paths=["md_staging"], max_files=1)
            processor = create_md_processor(config)
            test_results["md_processor_creation"] = "success"
            logger.info("  ✓ MD 프로세서 생성 성공")
        except Exception as e:
            test_results["md_processor_creation"] = f"failed: {e}"
            logger.warning(f"  ⚠ MD 프로세서 생성 실패: {e}")
        
        # OpenAI 커넥터 기본 테스트
        try:
            from openai_connector import create_openai_client, OpenAIAPIClientConfig
            config = OpenAIAPIClientConfig(
                endpoint="http://123.37.28.120:9997/v1",
                model="qwen2.5-vl-instruct"
            )
            client = create_openai_client(config)
            test_results["openai_connector_creation"] = "success"
            logger.info("  ✓ OpenAI 커넥터 생성 성공")
        except Exception as e:
            test_results["openai_connector_creation"] = f"failed: {e}"
            logger.warning(f"  ⚠ OpenAI 커넥터 생성 실패: {e}")
        
        # Unsloth 데이터셋 생성기 기본 테스트
        try:
            from unsloth_dataset import create_unsloth_generator, UnslothDatasetConfig
            config = UnslothDatasetConfig(formats=["sharegpt"])
            generator = create_unsloth_generator(config)
            test_results["unsloth_generator_creation"] = "success"
            logger.info("  ✓ Unsloth 생성기 생성 성공")
        except Exception as e:
            test_results["unsloth_generator_creation"] = f"failed: {e}"
            logger.warning(f"  ⚠ Unsloth 생성기 생성 실패: {e}")
        
    except Exception as e:
        test_results["basic_functionality"] = f"error: {e}"
        logger.error(f"  ✗ 기본 기능 테스트 오류: {e}")
    
    return test_results


async def test_data_processing():
    """데이터 처리 테스트"""
    logger.info("데이터 처리 테스트 중...")
    
    test_results = {}
    
    # 테스트용 대화 데이터 (포맷터가 기대하는 형식으로 수정)
    test_conversations = [
        {
            "id": "test_001",
            "instruction": "How do I use Syncfusion GridControl?",
            "input": "",
            "output": "To use Syncfusion GridControl, you need to create an instance and set up data binding.",
            "response": "To use Syncfusion GridControl, you need to create an instance and set up data binding.",
            "conversations": [
                {"from": "human", "value": "How do I use Syncfusion GridControl?"},
                {"from": "gpt", "value": "To use Syncfusion GridControl, you need to create an instance and set up data binding."}
            ],
            "metadata": {"component": "GridControl"}
        }
    ]
    
    try:
        # ShareGPT 포맷 변환 테스트
        try:
            from unsloth_dataset.formatters.sharegpt_formatter import ShareGPTFormatter
            formatter = ShareGPTFormatter()
            formatted_data = formatter.format(test_conversations)
            
            if formatted_data and len(formatted_data) > 0:
                test_results["sharegpt_formatting"] = "success"
                logger.info("  ✓ ShareGPT 포맷 변환 성공")
            else:
                test_results["sharegpt_formatting"] = "failed: empty result"
                logger.warning("  ⚠ ShareGPT 포맷 변환 결과 없음")
        except Exception as e:
            test_results["sharegpt_formatting"] = f"failed: {e}"
            logger.warning(f"  ⚠ ShareGPT 포맷 변환 실패: {e}")
        
        # Alpaca 포맷 변환 테스트
        try:
            from unsloth_dataset.formatters.alpaca_formatter import AlpacaFormatter
            formatter = AlpacaFormatter()
            formatted_data = formatter.format(test_conversations)
            
            if formatted_data and len(formatted_data) > 0:
                test_results["alpaca_formatting"] = "success"
                logger.info("  ✓ Alpaca 포맷 변환 성공")
            else:
                test_results["alpaca_formatting"] = "failed: empty result"
                logger.warning("  ⚠ Alpaca 포맷 변환 결과 없음")
        except Exception as e:
            test_results["alpaca_formatting"] = f"failed: {e}"
            logger.warning(f"  ⚠ Alpaca 포맷 변환 실패: {e}")
        
    except Exception as e:
        test_results["data_processing"] = f"error: {e}"
        logger.error(f"  ✗ 데이터 처리 테스트 오류: {e}")
    
    return test_results


async def main():
    """메인 함수"""
    logger.info("=== 간단한 통합 테스트 시작 ===")
    
    all_results = {}
    
    try:
        # 1. 모듈 임포트 테스트
        module_results = await test_module_imports()
        all_results["module_imports"] = module_results
        
        # 2. 파일 구조 테스트
        structure_results = await test_file_structure()
        all_results["file_structure"] = structure_results
        
        # 3. 기본 기능 테스트
        functionality_results = await test_basic_functionality()
        all_results["basic_functionality"] = functionality_results
        
        # 4. 데이터 처리 테스트
        processing_results = await test_data_processing()
        all_results["data_processing"] = processing_results
        
        # 결과 분석
        total_tests = 0
        passed_tests = 0
        failed_tests = 0
        
        for category, results in all_results.items():
            for test_name, result in results.items():
                total_tests += 1
                if result == "success" or result == "exists":
                    passed_tests += 1
                else:
                    failed_tests += 1
        
        # 결과 저장
        report = {
            "timestamp": datetime.now().isoformat(),
            "test_type": "simple_integration",
            "summary": {
                "total_tests": total_tests,
                "passed": passed_tests,
                "failed": failed_tests,
                "success_rate": passed_tests / total_tests if total_tests > 0 else 0
            },
            "detailed_results": all_results
        }
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"simple_integration_test_{timestamp}.json"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        # 결과 출력
        logger.info("=" * 60)
        logger.info("간단한 통합 테스트 결과")
        logger.info("=" * 60)
        logger.info(f"총 테스트: {total_tests}개")
        logger.info(f"성공: {passed_tests}개")
        logger.info(f"실패: {failed_tests}개")
        logger.info(f"성공률: {passed_tests / total_tests * 100:.1f}%" if total_tests > 0 else "성공률: 0%")
        logger.info(f"리포트 파일: {report_file}")
        logger.info("=" * 60)
        
        if passed_tests == total_tests:
            print(f"\n🎉 모든 테스트 통과! ({passed_tests}/{total_tests})")
            print("기본적인 시스템 구성이 완료되었습니다.")
        elif passed_tests >= total_tests * 0.8:
            print(f"\n✅ 대부분의 테스트 통과! ({passed_tests}/{total_tests})")
            print("시스템이 기본적으로 동작할 준비가 되었습니다.")
        else:
            print(f"\n⚠️ 일부 테스트 실패! ({passed_tests}/{total_tests})")
            print("시스템 설정을 확인해주세요.")
        
    except Exception as e:
        logger.error(f"테스트 실행 중 오류: {e}")
        print(f"\n❌ 테스트 실행 실패: {e}")
        sys.exit(1)
    
    logger.info("=== 간단한 통합 테스트 완료 ===")


if __name__ == "__main__":
    asyncio.run(main())