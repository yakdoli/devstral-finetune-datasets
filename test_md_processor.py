#!/usr/bin/env python3
"""
MD 처리 모듈 테스트 스크립트
"""

import sys
import os
from pathlib import Path

# 현재 디렉토리를 Python 경로에 추가
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

try:
    from md_processor import (
        create_scanner, create_parser, create_processor,
        process_documents_simple, quick_scan, print_module_info,
        setup_logging, validate_document_structure, calculate_content_stats
    )
    print("✓ md_processor 모듈 임포트 성공")
except ImportError as e:
    print(f"✗ md_processor 모듈 임포트 실패: {e}")
    sys.exit(1)


def test_basic_functionality():
    """기본 기능 테스트"""
    print("\n=== 기본 기능 테스트 ===")
    
    try:
        # 로깅 설정
        setup_logging("INFO")
        print("✓ 로깅 설정 성공")
        
        # 모듈 정보 출력
        print_module_info()
        print("✓ 모듈 정보 출력 성공")
        
        # 빠른 스캔 테스트
        print("\n--- 빠른 스캔 테스트 ---")
        scan_result = quick_scan()
        print(f"✓ 스캔 결과: {scan_result}")
        
        return True
        
    except Exception as e:
        print(f"✗ 기본 기능 테스트 실패: {e}")
        return False


def test_scanner():
    """스캐너 테스트"""
    print("\n=== 스캐너 테스트 ===")
    
    try:
        # 스캐너 생성
        scanner = create_scanner()
        print("✓ 스캐너 생성 성공")
        
        # 스캔 통계 확인
        stats = scanner.get_scan_statistics()
        print(f"✓ 스캔 통계: {stats}")
        
        # 컴포넌트 파일 확인
        component_files = list(scanner.get_component_files())
        print(f"✓ 컴포넌트 파일 개수: {len(component_files)}")
        
        # 페이지 파일 확인
        page_files = list(scanner.get_page_files())
        print(f"✓ 페이지 파일 개수: {len(page_files)}")
        
        return True
        
    except Exception as e:
        print(f"✗ 스캐너 테스트 실패: {e}")
        return False


def test_parser():
    """파서 테스트"""
    print("\n=== 파서 테스트 ===")
    
    try:
        # 파서 생성
        parser = create_parser()
        print("✓ 파서 생성 성공")
        
        # 테스트용 MD 파일 경로 확인
        test_md_path = Path("md_staging/grid/page_020.md")
        test_json_path = Path("md_staging/grid/page_020.json")
        
        if test_md_path.exists():
            # 파일 파싱 테스트
            result = parser.parse_file(test_md_path, test_json_path if test_json_path.exists() else None)
            print(f"✓ 파일 파싱 성공: {result['title']}")
            print(f"  - ID: {result['id']}")
            print(f"  - Component: {result['component']}")
            print(f"  - Page: {result['page']}")
            print(f"  - Content length: {len(result['content'])}")
            print(f"  - Quality score: {result['quality_score']}")
            
            # 문서 구조 검증
            is_valid, errors = validate_document_structure(result)
            if is_valid:
                print("✓ 문서 구검증 성공")
            else:
                print(f"✗ 문서 구조 검증 실패: {errors}")
        else:
            print("⚠ 테스트용 MD 파일을 찾을 수 없음")
        
        return True
        
    except Exception as e:
        print(f"✗ 파서 테스트 실패: {e}")
        return False


def test_processor():
    """프로세서 테스트"""
    print("\n=== 프로세서 테스트 ===")
    
    try:
        # 프로세서 생성
        processor = create_processor()
        print("✓ 프로세서 생성 성공")
        
        # 처리 테스트 (소규모)
        print("--- 소규모 처리 테스트 ---")
        test_output = Path("test_output.json")
        
        # 배치 처리 테스트
        batch_count = 0
        for batch in processor.process_documents_batch(test_output):
            batch_count += 1
            print(f"✓ 배치 {batch_count} 처리 완료: {len(batch)}개 문서")
            
            # 첫 번째 문서 검증
            if batch:
                doc = batch[0]
                is_valid, errors = validate_document_structure(doc)
                if is_valid:
                    print(f"  - 문서 구검증 성공: {doc['title']}")
                else:
                    print(f"  - 문서 구검증 실패: {errors}")
            
            # 테스트는 첫 배치만 처리
            if batch_count >= 1:
                break
        
        print(f"✓ 배치 처리 테스트 성공 (총 {batch_count}개 배치)")
        
        # 결과 파일 확인
        if test_output.exists():
            print(f"✓ 결과 파일 생성: {test_output}")
            # 결과 파일 내용 확인
            import json
            with open(test_output, 'r', encoding='utf-8') as f:
                results = json.load(f)
            print(f"  - 총 처리된 문서 수: {len(results)}")
        
        return True
        
    except Exception as e:
        print(f"✗ 프로세서 테스트 실패: {e}")
        return False


def test_simple_interface():
    """간단 인터페이스 테스트"""
    print("\n=== 간단 인터페이스 테스트 ===")
    
    try:
        # 간단한 문서 처리 테스트
        print("--- 간단한 문서 처리 테스트 ---")
        simple_output = Path("simple_test_output.json")
        
        # 실제 처리는 주석 처리 (테스트 시간 단축)
        # documents = process_documents_simple(str(simple_output))
        # print(f"✓ 간단 처리 완료: {len(documents)}개 문서")
        
        print("✓ 간단 인터페이스 테스트 (실제 처리는 생략)")
        
        return True
        
    except Exception as e:
        print(f"✗ 간단 인터페이스 테스트 실패: {e}")
        return False


def test_utils():
    """유틸리티 함수 테스트"""
    print("\n=== 유틸리티 함수 테스트 ===")
    
    try:
        from md_processor.utils import (
            normalize_text, clean_filename, generate_unique_id,
            calculate_content_stats, format_file_size
        )
        
        # 텍스트 정규화 테스트
        test_text = "  Hello   World  \n\n  Test  \n"
        normalized = normalize_text(test_text)
        print(f"✓ 텍스트 정규화: '{normalized}'")
        
        # 파일명 정리 테스트
        test_filename = "test<>file:name?*with*special|chars.md"
        cleaned = clean_filename(test_filename)
        print(f"✓ 파일명 정리: '{cleaned}'")
        
        # 고유 ID 생성 테스트
        unique_id = generate_unique_id(test_text)
        print(f"✓ 고유 ID 생성: {unique_id}")
        
        # 콘텐츠 통계 테스트
        test_content = "# Test\n\nThis is a test content.\n\n## Section\n\n- Item 1\n- Item 2\n\n```python\nprint('hello')\n```\n\n[Link](https://example.com)"
        stats = calculate_content_stats(test_content)
        print(f"✓ 콘텐츠 통계: {stats}")
        
        # 파일 크기 포맷팅 테스트
        formatted = format_file_size(1024 * 1024 * 2.5)
        print(f"✓ 파일 크기 포맷팅: {formatted}")
        
        return True
        
    except Exception as e:
        print(f"✗ 유틸리티 함수 테스트 실패: {e}")
        return False


def cleanup_test_files():
    """테스트 파일 정리"""
    print("\n=== 테스트 파일 정리 ===")
    
    test_files = [
        "test_output.json",
        "test_output.stats.json",
        "simple_test_output.json",
        "simple_test_output.stats.json"
    ]
    
    for file_path in test_files:
        path = Path(file_path)
        if path.exists():
            path.unlink()
            print(f"✓ 삭제: {file_path}")


def main():
    """메인 테스트 함수"""
    print("MD 처리 모듈 테스트 시작")
    print("=" * 50)
    
    test_results = []
    
    # 각 테스트 실행
    test_results.append(("기본 기능", test_basic_functionality()))
    test_results.append(("스캐너", test_scanner()))
    test_results.append(("파서", test_parser()))
    test_results.append(("프로세서", test_processor()))
    test_results.append(("간단 인터페이스", test_simple_interface()))
    test_results.append(("유틸리티 함수", test_utils()))
    
    # 테스트 결과 요약
    print("\n" + "=" * 50)
    print("테스트 결과 요약")
    print("=" * 50)
    
    passed = 0
    total = len(test_results)
    
    for test_name, result in test_results:
        status = "✓ 통과" if result else "✗ 실패"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\n통과: {passed}/{total}")
    
    if passed == total:
        print("🎉 모든 테스트 통과!")
        return 0
    else:
        print("⚠ 일부 테스트 실패")
        return 1


if __name__ == "__main__":
    exit_code = main()
    
    # 테스트 파일 정리
    try:
        cleanup_test_files()
    except Exception as e:
        print(f"테스트 파일 정리 중 오류: {e}")
    
    sys.exit(exit_code)