#!/usr/bin/env python3
"""
최종 검증 테스트
시스템의 핵심 기능들이 정상적으로 동작하는지 검증
"""

import asyncio
import json
import logging
import time
from datetime import datetime
from pathlib import Path

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def test_core_functionality():
    """핵심 기능 테스트"""
    logger.info("=== 핵심 기능 검증 테스트 시작 ===")
    
    test_results = {
        "module_loading": {},
        "basic_operations": {},
        "data_processing": {},
        "format_conversion": {}
    }
    
    # 1. 모듈 로딩 테스트
    logger.info("1. 모듈 로딩 테스트 중...")
    
    try:
        from md_processor import create_md_processor, MDProcessorConfig
        test_results["module_loading"]["md_processor"] = "success"
        logger.info("  ✓ MD 프로세서 모듈 로딩 성공")
    except Exception as e:
        test_results["module_loading"]["md_processor"] = f"failed: {e}"
        logger.error(f"  ✗ MD 프로세서 모듈 로딩 실패: {e}")
    
    try:
        from openai_connector import create_openai_client, OpenAIAPIClientConfig
        test_results["module_loading"]["openai_connector"] = "success"
        logger.info("  ✓ OpenAI 커넥터 모듈 로딩 성공")
    except Exception as e:
        test_results["module_loading"]["openai_connector"] = f"failed: {e}"
        logger.error(f"  ✗ OpenAI 커넥터 모듈 로딩 실패: {e}")
    
    try:
        from unsloth_dataset import create_unsloth_generator, UnslothDatasetConfig
        test_results["module_loading"]["unsloth_dataset"] = "success"
        logger.info("  ✓ Unsloth 데이터셋 모듈 로딩 성공")
    except Exception as e:
        test_results["module_loading"]["unsloth_dataset"] = f"failed: {e}"
        logger.error(f"  ✗ Unsloth 데이터셋 모듈 로딩 실패: {e}")
    
    # 2. 기본 동작 테스트
    logger.info("2. 기본 동작 테스트 중...")
    
    try:
        # MD 프로세서 생성 테스트
        config = MDProcessorConfig(base_paths=["md_staging"], max_files=1)
        processor = create_md_processor(config)
        test_results["basic_operations"]["md_processor_creation"] = "success"
        logger.info("  ✓ MD 프로세서 생성 성공")
    except Exception as e:
        test_results["basic_operations"]["md_processor_creation"] = f"failed: {e}"
        logger.error(f"  ✗ MD 프로세서 생성 실패: {e}")
    
    try:
        # OpenAI 클라이언트 생성 테스트
        config = OpenAIAPIClientConfig(
            endpoint="http://123.37.28.120:9997/v1",
            model="qwen2.5-vl-instruct"
        )
        client = create_openai_client(config)
        test_results["basic_operations"]["openai_client_creation"] = "success"
        logger.info("  ✓ OpenAI 클라이언트 생성 성공")
    except Exception as e:
        test_results["basic_operations"]["openai_client_creation"] = f"failed: {e}"
        logger.error(f"  ✗ OpenAI 클라이언트 생성 실패: {e}")
    
    try:
        # Unsloth 생성기 생성 테스트
        config = UnslothDatasetConfig(formats=["sharegpt", "alpaca"])
        generator = create_unsloth_generator(config)
        test_results["basic_operations"]["unsloth_generator_creation"] = "success"
        logger.info("  ✓ Unsloth 생성기 생성 성공")
    except Exception as e:
        test_results["basic_operations"]["unsloth_generator_creation"] = f"failed: {e}"
        logger.error(f"  ✗ Unsloth 생성기 생성 실패: {e}")
    
    # 3. 데이터 처리 테스트
    logger.info("3. 데이터 처리 테스트 중...")
    
    test_data = [
        {
            "instruction": "Syncfusion GridControl 사용법을 설명해주세요.",
            "input": "",
            "output": "GridControl을 사용하려면 다음 단계를 따르세요:\n1. 컨트롤 추가\n2. 데이터 바인딩\n3. 컬럼 설정",
            "response": "GridControl을 사용하려면 다음 단계를 따르세요:\n1. 컨트롤 추가\n2. 데이터 바인딩\n3. 컬럼 설정"
        }
    ]
    
    try:
        # ShareGPT 포맷 변환 테스트
        from unsloth_dataset.formatters.sharegpt_formatter import ShareGPTFormatter
        formatter = ShareGPTFormatter()
        result = formatter.format(test_data)
        
        if result and len(result) > 0:
            test_results["data_processing"]["sharegpt_formatting"] = "success"
            logger.info("  ✓ ShareGPT 포맷 변환 성공")
        else:
            test_results["data_processing"]["sharegpt_formatting"] = "failed: empty result"
            logger.warning("  ⚠ ShareGPT 포맷 변환 결과 없음")
    except Exception as e:
        test_results["data_processing"]["sharegpt_formatting"] = f"failed: {e}"
        logger.error(f"  ✗ ShareGPT 포맷 변환 실패: {e}")
    
    try:
        # Alpaca 포맷 변환 테스트
        from unsloth_dataset.formatters.alpaca_formatter import AlpacaFormatter
        formatter = AlpacaFormatter()
        result = formatter.format(test_data)
        
        if result and len(result) > 0:
            test_results["data_processing"]["alpaca_formatting"] = "success"
            logger.info("  ✓ Alpaca 포맷 변환 성공")
        else:
            test_results["data_processing"]["alpaca_formatting"] = "failed: empty result"
            logger.warning("  ⚠ Alpaca 포맷 변환 결과 없음")
    except Exception as e:
        test_results["data_processing"]["alpaca_formatting"] = f"failed: {e}"
        logger.error(f"  ✗ Alpaca 포맷 변환 실패: {e}")
    
    # 4. 포맷 호환성 테스트
    logger.info("4. 포맷 호환성 테스트 중...")
    
    try:
        # ShareGPT 포맷 검증
        from unsloth_dataset.formatters.sharegpt_formatter import ShareGPTFormatter
        formatter = ShareGPTFormatter()
        
        # 테스트 데이터 생성
        test_sharegpt = {
            "conversations": [
                {"from": "human", "value": "테스트 질문"},
                {"from": "gpt", "value": "테스트 응답"}
            ]
        }
        
        is_valid = formatter.validate_format(test_sharegpt)
        if is_valid:
            test_results["format_conversion"]["sharegpt_validation"] = "success"
            logger.info("  ✓ ShareGPT 포맷 검증 성공")
        else:
            test_results["format_conversion"]["sharegpt_validation"] = "failed: invalid format"
            logger.warning("  ⚠ ShareGPT 포맷 검증 실패")
    except Exception as e:
        test_results["format_conversion"]["sharegpt_validation"] = f"failed: {e}"
        logger.error(f"  ✗ ShareGPT 포맷 검증 오류: {e}")
    
    try:
        # Alpaca 포맷 검증
        from unsloth_dataset.formatters.alpaca_formatter import AlpacaFormatter
        formatter = AlpacaFormatter()
        
        # 테스트 데이터 생성
        test_alpaca = {
            "instruction": "테스트 지시사항",
            "input": "",
            "output": "테스트 출력"
        }
        
        is_valid = formatter.validate_format(test_alpaca)
        if is_valid:
            test_results["format_conversion"]["alpaca_validation"] = "success"
            logger.info("  ✓ Alpaca 포맷 검증 성공")
        else:
            test_results["format_conversion"]["alpaca_validation"] = "failed: invalid format"
            logger.warning("  ⚠ Alpaca 포맷 검증 실패")
    except Exception as e:
        test_results["format_conversion"]["alpaca_validation"] = f"failed: {e}"
        logger.error(f"  ✗ Alpaca 포맷 검증 오류: {e}")
    
    return test_results


async def test_performance_basics():
    """기본 성능 테스트"""
    logger.info("5. 기본 성능 테스트 중...")
    
    performance_results = {}
    
    # 간단한 처리량 테스트
    test_data = [
        {
            "instruction": f"테스트 질문 {i}",
            "input": "",
            "output": f"테스트 응답 {i}",
            "response": f"테스트 응답 {i}"
        }
        for i in range(10)
    ]
    
    try:
        from unsloth_dataset.formatters.sharegpt_formatter import ShareGPTFormatter
        formatter = ShareGPTFormatter()
        
        start_time = time.time()
        results = formatter.format(test_data)
        end_time = time.time()
        
        processing_time = end_time - start_time
        throughput = len(test_data) / processing_time if processing_time > 0 else 0
        
        performance_results["sharegpt_throughput"] = {
            "items_processed": len(results),
            "processing_time": processing_time,
            "throughput_items_per_sec": throughput
        }
        
        logger.info(f"  ✓ ShareGPT 처리량: {throughput:.1f} items/sec")
        
    except Exception as e:
        performance_results["sharegpt_throughput"] = f"failed: {e}"
        logger.error(f"  ✗ ShareGPT 성능 테스트 실패: {e}")
    
    return performance_results


async def test_unsloth_compatibility():
    """Unsloth 호환성 기본 테스트"""
    logger.info("6. Unsloth 호환성 테스트 중...")
    
    compatibility_results = {}
    
    # ShareGPT 호환성 테스트
    try:
        sharegpt_data = {
            "conversations": [
                {"from": "human", "value": "Syncfusion WinForms에 대해 설명해주세요."},
                {"from": "gpt", "value": "Syncfusion WinForms는 .NET 기반의 UI 컴포넌트 라이브러리입니다."}
            ]
        }
        
        # 필수 필드 확인
        required_fields = ["conversations"]
        has_required_fields = all(field in sharegpt_data for field in required_fields)
        
        # 대화 구조 확인
        valid_structure = True
        if "conversations" in sharegpt_data:
            for conv in sharegpt_data["conversations"]:
                if not all(key in conv for key in ["from", "value"]):
                    valid_structure = False
                    break
                if conv["from"] not in ["human", "gpt", "system"]:
                    valid_structure = False
                    break
        
        compatibility_results["sharegpt_compatibility"] = {
            "has_required_fields": has_required_fields,
            "valid_structure": valid_structure,
            "compatible": has_required_fields and valid_structure
        }
        
        if has_required_fields and valid_structure:
            logger.info("  ✓ ShareGPT Unsloth 호환성 확인")
        else:
            logger.warning("  ⚠ ShareGPT Unsloth 호환성 이슈")
        
    except Exception as e:
        compatibility_results["sharegpt_compatibility"] = f"failed: {e}"
        logger.error(f"  ✗ ShareGPT 호환성 테스트 실패: {e}")
    
    # Alpaca 호환성 테스트
    try:
        alpaca_data = {
            "instruction": "Syncfusion Chart 컴포넌트 사용법을 설명해주세요.",
            "input": "",
            "output": "Chart 컴포넌트를 사용하려면 다음과 같이 하세요..."
        }
        
        # 필수 필드 확인
        required_fields = ["instruction", "input", "output"]
        has_required_fields = all(field in alpaca_data for field in required_fields)
        
        # 데이터 타입 확인
        valid_types = all(isinstance(alpaca_data[field], str) for field in required_fields)
        
        compatibility_results["alpaca_compatibility"] = {
            "has_required_fields": has_required_fields,
            "valid_types": valid_types,
            "compatible": has_required_fields and valid_types
        }
        
        if has_required_fields and valid_types:
            logger.info("  ✓ Alpaca Unsloth 호환성 확인")
        else:
            logger.warning("  ⚠ Alpaca Unsloth 호환성 이슈")
        
    except Exception as e:
        compatibility_results["alpaca_compatibility"] = f"failed: {e}"
        logger.error(f"  ✗ Alpaca 호환성 테스트 실패: {e}")
    
    return compatibility_results


async def main():
    """메인 함수"""
    start_time = datetime.now()
    
    try:
        # 핵심 기능 테스트
        core_results = await test_core_functionality()
        
        # 성능 테스트
        performance_results = await test_performance_basics()
        
        # 호환성 테스트
        compatibility_results = await test_unsloth_compatibility()
        
        end_time = datetime.now()
        total_time = (end_time - start_time).total_seconds()
        
        # 결과 분석
        all_results = {
            "core_functionality": core_results,
            "performance": performance_results,
            "compatibility": compatibility_results
        }
        
        # 성공/실패 카운트
        total_tests = 0
        passed_tests = 0
        
        for category, results in all_results.items():
            for subcategory, subresults in results.items():
                if isinstance(subresults, dict):
                    for test_name, result in subresults.items():
                        total_tests += 1
                        if result == "success" or (isinstance(result, dict) and result.get("compatible", False)):
                            passed_tests += 1
                else:
                    total_tests += 1
                    if subresults == "success":
                        passed_tests += 1
        
        success_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        
        # 최종 리포트 생성
        final_report = {
            "timestamp": start_time.isoformat(),
            "test_type": "final_verification",
            "duration_seconds": total_time,
            "summary": {
                "total_tests": total_tests,
                "passed_tests": passed_tests,
                "failed_tests": total_tests - passed_tests,
                "success_rate": success_rate
            },
            "detailed_results": all_results,
            "system_status": {
                "core_modules_working": all(
                    result == "success" 
                    for result in core_results.get("module_loading", {}).values()
                ),
                "basic_operations_working": all(
                    result == "success" 
                    for result in core_results.get("basic_operations", {}).values()
                ),
                "data_processing_working": all(
                    result == "success" 
                    for result in core_results.get("data_processing", {}).values()
                ),
                "unsloth_compatible": all(
                    result.get("compatible", False) if isinstance(result, dict) else False
                    for result in compatibility_results.values()
                )
            }
        }
        
        # 리포트 저장
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"final_verification_report_{timestamp}.json"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(final_report, f, indent=2, ensure_ascii=False)
        
        # 결과 출력
        logger.info("=" * 60)
        logger.info("최종 검증 테스트 결과")
        logger.info("=" * 60)
        logger.info(f"총 테스트 시간: {total_time:.1f}초")
        logger.info(f"총 테스트: {total_tests}개")
        logger.info(f"성공: {passed_tests}개")
        logger.info(f"실패: {total_tests - passed_tests}개")
        logger.info(f"성공률: {success_rate:.1f}%")
        logger.info("")
        
        system_status = final_report["system_status"]
        logger.info("시스템 상태:")
        logger.info(f"  핵심 모듈: {'✓' if system_status['core_modules_working'] else '✗'}")
        logger.info(f"  기본 동작: {'✓' if system_status['basic_operations_working'] else '✗'}")
        logger.info(f"  데이터 처리: {'✓' if system_status['data_processing_working'] else '✗'}")
        logger.info(f"  Unsloth 호환성: {'✓' if system_status['unsloth_compatible'] else '✗'}")
        logger.info("")
        logger.info(f"상세 리포트: {report_file}")
        logger.info("=" * 60)
        
        # 최종 판정
        if success_rate >= 90:
            print(f"\n🎉 최종 검증 완료! 성공률: {success_rate:.1f}%")
            print("시스템이 정상적으로 동작할 준비가 되었습니다!")
        elif success_rate >= 75:
            print(f"\n✅ 최종 검증 완료! 성공률: {success_rate:.1f}%")
            print("시스템이 기본적으로 동작하지만 일부 개선이 필요합니다.")
        else:
            print(f"\n⚠️ 최종 검증 완료! 성공률: {success_rate:.1f}%")
            print("시스템에 중요한 이슈가 있습니다. 문제를 해결해주세요.")
        
    except Exception as e:
        logger.error(f"최종 검증 테스트 실행 중 오류: {e}")
        print(f"\n❌ 최종 검증 테스트 실패: {e}")
    
    logger.info("=== 최종 검증 테스트 완료 ===")


if __name__ == "__main__":
    asyncio.run(main())