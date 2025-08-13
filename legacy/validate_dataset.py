#!/usr/bin/env python3
"""
데이터셋 검증 스크립트
"""

import json
from pathlib import Path

def validate_dataset():
    """데이터셋 검증"""
    dataset_path = Path('syncfusion_tool_calling_dataset.json')
    
    if not dataset_path.exists():
        print("❌ 데이터셋 파일이 존재하지 않습니다.")
        return False
    
    try:
        with open(dataset_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ 데이터셋 로드 실패: {e}")
        return False
    
    print("=== 데이터셋 검증 결과 ===")
    print(f"✅ 총 샘플 수: {len(data)}")
    
    # 도구 사용 통계
    tool_usage = {}
    for sample in data:
        for tool_call in sample.get('tool_calls', []):
            tool_name = tool_call.get('function', {}).get('name', 'unknown')
            tool_usage[tool_name] = tool_usage.get(tool_name, 0) + 1
    
    print("\n🔧 도구 사용 통계:")
    for tool_name, count in tool_usage.items():
        print(f"  {tool_name}: {count}회")
    
    # 컴포넌트별 분석
    grid_samples = [s for s in data if 'grid' in s.get('output', '').lower()]
    chart_samples = [s for s in data if 'chart' in s.get('output', '').lower()]
    xlsio_samples = [s for s in data if 'xlsio' in s.get('output', '').lower()]
    
    print(f"\n📊 컴포넌트별 샘플 수:")
    print(f"  그리드 관련: {len(grid_samples)}개")
    print(f"  차트 관련: {len(chart_samples)}개")
    print(f"  Excel 관련: {len(xlsio_samples)}개")
    
    # Context7 데이터 통합 확인
    context7_samples = [s for s in data if 'Basic Grid Configuration' in s.get('output', '')]
    print(f"\n🔗 Context7 데이터 통합: {len(context7_samples)}개")
    
    # 데이터 형식 검증
    required_fields = ['instruction', 'input', 'output', 'tools', 'tool_calls']
    valid_samples = 0
    
    for i, sample in enumerate(data[:10]):  # 첫 10개 샘플만 검증
        if all(field in sample for field in required_fields):
            valid_samples += 1
        else:
            print(f"⚠️  샘플 {i+1} 필드 누락: {set(required_fields) - set(sample.keys())}")
    
    print(f"\n✅ 데이터 형식 검증: {valid_samples}/10 샘플 유효")
    
    # 샘플 출력
    print("\n📝 샘플 데이터:")
    for i, sample in enumerate(data[:2]):
        print(f"\n[샘플 {i+1}]")
        print(f"Instruction: {sample['instruction']}")
        print(f"Tool Calls: {[tc['function']['name'] for tc in sample['tool_calls']]}")
        print(f"Output: {sample['output'][:100]}...")
    
    return True

if __name__ == "__main__":
    validate_dataset()