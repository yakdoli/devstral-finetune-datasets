import json
import os

def validate_alpaca_dataset(file_path):
    """Alpaca 형식 데이터셋 검증"""
    print(f"=== Alpaca 데이터셋 검증: {file_path} ===")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"메타데이터: {data['metadata']}")
        print(f"데이터셋 크기: {len(data['dataset'])}개 항목")
        print(f"첫 번째 항목 구조: {list(data['dataset'][0].keys())}")
        
        # 데이터 무결성 검사
        required_fields = ['instruction', 'input', 'output']
        valid_items = []
        invalid_items = []
        
        for i, item in enumerate(data['dataset']):
            if all(field in item for field in required_fields):
                valid_items.append(i)
            else:
                invalid_items.append(i)
        
        print(f"유효한 항목: {len(valid_items)}개")
        print(f"유효하지 않은 항목: {len(invalid_items)}개")
        
        if invalid_items:
            print(f"유효하지 않은 항목 인덱스: {invalid_items}")
        
        # JSON 유효성 검사
        try:
            json.dumps(data)
            print("JSON 유효성: ✓ 통과")
            return True
        except Exception as e:
            print(f"JSON 유효성: ✗ 실패 - {e}")
            return False
            
    except Exception as e:
        print(f"데이터셋 로딩 실패: {e}")
        return False

def validate_sharegpt_dataset(file_path):
    """ShareGPT 형식 데이터셋 검증"""
    print(f"\n=== ShareGPT 데이터셋 검증: {file_path} ===")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"메타데이터: {data['metadata']}")
        print(f"데이터셋 크기: {len(data['dataset'])}개 항목")
        print(f"첫 번째 항목 구조: {list(data['dataset'][0].keys())}")
        
        # 데이터 무결성 검사
        valid_items = []
        invalid_items = []
        
        for i, item in enumerate(data['dataset']):
            if 'conversations' in item and len(item['conversations']) == 2:
                # 각 conversation의 필드 검사
                valid_convo = True
                for convo in item['conversations']:
                    if 'from' not in convo or 'value' not in convo:
                        valid_convo = False
                        break
                
                if valid_convo:
                    valid_items.append(i)
                else:
                    invalid_items.append(i)
            else:
                invalid_items.append(i)
        
        print(f"유효한 항목: {len(valid_items)}개")
        print(f"유효하지 않은 항목: {len(invalid_items)}개")
        
        if invalid_items:
            print(f"유효하지 않은 항목 인덱스: {invalid_items}")
        
        # JSON 유효성 검사
        try:
            json.dumps(data)
            print("JSON 유효성: ✓ 통과")
            return True
        except Exception as e:
            print(f"JSON 유효성: ✗ 실패 - {e}")
            return False
            
    except Exception as e:
        print(f"데이터셋 로딩 실패: {e}")
        return False

def main():
    """메인 검증 함수"""
    alpaca_file = 'syncfusion_winforms_alpaca_dataset.json'
    sharegpt_file = 'syncfusion_winforms_sharegpt_dataset.json'
    
    # 파일 존재 확인
    if not os.path.exists(alpaca_file):
        print(f"오류: {alpaca_file} 파일이 존재하지 않습니다")
        return
    
    if not os.path.exists(sharegpt_file):
        print(f"오류: {sharegpt_file} 파일이 존재하지 않습니다")
        return
    
    # 데이터셋 검증
    alpaca_valid = validate_alpaca_dataset(alpaca_file)
    sharegpt_valid = validate_sharegpt_dataset(sharegpt_file)
    
    # 최종 결과
    print(f"\n=== 최종 검증 결과 ===")
    print(f"Alpaca 데이터셋: {'✓ 통과' if alpaca_valid else '✗ 실패'}")
    print(f"ShareGPT 데이터셋: {'✓ 통과' if sharegpt_valid else '✗ 실패'}")
    
    if alpaca_valid and sharegpt_valid:
        print("\n🎉 모든 데이터셋 검증이 성공적으로 완료되었습니다!")
    else:
        print("\n⚠️ 일부 데이터셋 검증에 실패했습니다. 수정이 필요합니다.")

if __name__ == "__main__":
    main()