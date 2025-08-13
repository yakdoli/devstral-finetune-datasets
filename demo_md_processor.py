#!/usr/bin/env python3
"""
MD 처리 모듈 데모 스크립트
실제 문서 처리를 보여주는 간단한 데모
"""

import sys
from pathlib import Path

# 현재 디렉토리를 Python 경로에 추가
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

from md_processor import (
    create_scanner, create_parser, create_processor,
    setup_logging, process_documents_simple
)


def main():
    """메인 데모 함수"""
    print("MD 처리 모듈 데모")
    print("=" * 50)
    
    # 로깅 설정
    setup_logging("INFO")
    
    # 1. 스캐너 데모
    print("\n1. 파일 스캔 데모")
    print("-" * 30)
    
    scanner = create_scanner()
    stats = scanner.get_scan_statistics()
    
    print(f"총 MD 파일: {stats['total_md_files']}")
    print(f"총 JSON 파일: {stats['total_json_files']}")
    print(f"스캔된 디렉토리: {stats['directories_scanned']}")
    
    # 2. 파서 데모
    print("\n2. 파싱 데모")
    print("-" * 30)
    
    parser = create_parser()
    
    # 실제 파일이 있는지 확인
    test_md_path = Path("md_staging/grid/page_020.md")
    test_json_path = Path("md_staging/grid/page_020.json")
    
    if test_md_path.exists():
        print(f"파일 파싱 중: {test_md_path}")
        result = parser.parse_file(test_md_path, test_json_path if test_json_path.exists() else None)
        
        print(f"✓ 파싱 성공!")
        print(f"  - 제목: {result['title']}")
        print(f"  - 컴포넌트: {result['component']}")
        print(f"  - 페이지: {result['page']}")
        print(f"  - 콘텐츠 길이: {len(result['content'])}")
        print(f"  - 품질 점수: {result['quality_score']:.2f}")
        
        # 콘텐츠 미리보기
        if result['content']:
            preview = result['content'][:200].replace('\n', ' ')
            print(f"  - 콘텐츠 미리보기: ...{preview}...")
    else:
        print("테스트 파일을 찾을 수 없습니다.")
    
    # 3. 프로세서 데모 (소규모)
    print("\n3. 처리 데모 (소규모)")
    print("-" * 30)
    
    processor = create_processor()
    
    # 소규모 배치 처리
    demo_output = Path("demo_output.json")
    batch_count = 0
    total_docs = 0
    
    print("소규모 배치 처리 시작...")
    for batch in processor.process_documents_batch(demo_output):
        batch_count += 1
        total_docs += len(batch)
        print(f"  - 배치 {batch_count}: {len(batch)}개 문서 처리")
        
        # 첫 번째 배치의 첫 번째 문서 정보 출력
        if batch and batch_count == 1:
            doc = batch[0]
            print(f"    - 예시 문서: {doc['title']}")
            print(f"    - 품질 점수: {doc['quality_score']:.2f}")
        
        # 데모는 최대 3개 배치만 처리
        if batch_count >= 3:
            break
    
    print(f"✓ 소규모 처리 완료: {batch_count}개 배치, {total_docs}개 문서")
    
    # 4. 결과 확인
    if demo_output.exists():
        print(f"\n4. 결과 확인")
        print("-" * 30)
        
        import json
        with open(demo_output, 'r', encoding='utf-8') as f:
            results = json.load(f)
        
        print(f"총 처리된 문서 수: {len(results)}")
        
        if results:
            # 품질 점수 통계
            quality_scores = [doc['quality_score'] for doc in results]
            avg_quality = sum(quality_scores) / len(quality_scores)
            max_quality = max(quality_scores)
            min_quality = min(quality_scores)
            
            print(f"품질 점수 통계:")
            print(f"  - 평균: {avg_quality:.2f}")
            print(f"  - 최대: {max_quality:.2f}")
            print(f"  - 최소: {min_quality:.2f}")
            
            # 컴포넌트별 통계
            components = {}
            for doc in results:
                comp = doc.get('component', 'Unknown')
                components[comp] = components.get(comp, 0) + 1
            
            print(f"\n컴포넌트별 문서 수:")
            for comp, count in sorted(components.items()):
                print(f"  - {comp}: {count}개")
    
    print(f"\n✓ 데모 완료!")
    print(f"결과 파일: {demo_output}")
    
    # 5. 정리
    print(f"\n5. 정리")
    print("-" * 30)
    
    # 데모 파일 삭제
    if demo_output.exists():
        demo_output.unlink()
        print(f"✓ 데모 파일 삭제: {demo_output}")
    
    print("\n" + "=" * 50)
    print("데모가 성공적으로 완료되었습니다!")
    print("MD 처리 모듈이 정상적으로 작동합니다.")


if __name__ == "__main__":
    main()