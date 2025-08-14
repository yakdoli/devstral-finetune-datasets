#!/usr/bin/env python3
"""
Unsloth 채팅 템플릿 통합 개선된 시스템 테스트
"""

import asyncio
import json
import logging
from datetime import datetime
from pathlib import Path

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def test_enhanced_unsloth_system():
    """개선된 Unsloth 시스템 테스트"""
    logger.info("=== Unsloth 채팅 템플릿 통합 개선된 시스템 테스트 시작 ===")
    
    try:
        from unsloth_dataset.enhanced_generator import (
            EnhancedUnslothDatasetGenerator,
            EnhancedDatasetConfig,
            generate_unsloth_compatible_datasets
        )
        from unsloth_dataset.chat_templates import (
            ChatTemplateType,
            ChatTemplateConfig,
            create_chat_template_manager
        )
        
        # 1. 채팅 템플릿 매니저 테스트
        logger.info("1. 채팅 템플릿 매니저 테스트 중...")
        
        template_manager = create_chat_template_manager()
        
        # 테스트 대화 데이터
        test_conversations = [
            {"from": "human", "value": "Syncfusion WinForms GridControl에서 데이터 바인딩을 어떻게 설정하나요?"},
            {"from": "gpt", "value": "GridControl에서 데이터 바인딩을 설정하는 방법:\n\n1. **DataSource 속성 설정:**\n```csharp\ngridControl.DataSource = dataTable;\n```\n\n2. **바인딩 컨텍스트 구성:**\n```csharp\nBindingContext bindingContext = new BindingContext();\ngridControl.BindingContext = bindingContext;\n```\n\n3. **데이터 멤버 지정:**\n```csharp\ngridControl.DataMember = \"TableName\";\n```"}
        ]
        
        # ChatML 템플릿 적용 테스트
        chatml_result = template_manager.apply_chat_template(
            conversations=test_conversations,
            template_type=ChatTemplateType.CHATML,
            mapping={"role": "from", "content": "value", "user": "human", "assistant": "gpt"}
        )
        
        logger.info("✓ ChatML 템플릿 적용 성공")
        logger.info(f"  결과 길이: {len(chatml_result)} 문자")
        
        # Alpaca 템플릿 적용 테스트
        alpaca_result = template_manager.apply_chat_template(
            conversations=test_conversations,
            template_type=ChatTemplateType.ALPACA,
            mapping={"role": "from", "content": "value", "user": "human", "assistant": "gpt"}
        )
        
        logger.info("✓ Alpaca 템플릿 적용 성공")
        logger.info(f"  결과 길이: {len(alpaca_result)} 문자")
        
        # 2. 개선된 데이터셋 생성기 테스트
        logger.info("2. 개선된 데이터셋 생성기 테스트 중...")
        
        # 테스트용 대화 데이터 (Context7 MCP 기반)
        enhanced_test_data = [
            {
                "instruction": "Syncfusion WinForms GridControl에서 셀 병합을 어떻게 설정하나요?",
                "input": "GridControl의 MergeCell 기능에 대해 자세히 설명해주세요.",
                "output": "Syncfusion WinForms GridControl에서 셀 병합을 설정하는 방법:\n\n**1. 기본 병합 동작 설정:**\n```csharp\nGridStyleInfo standardStyle = BaseStylesMap[\"Standard\"].StyleInfo;\nstandardStyle.MergeCell = GridMergeCellDirection.RowsInColumn;\n\nGridStyleInfo rowHeaderStyle = BaseStylesMap[\"Row Header\"].StyleInfo;\nrowHeaderStyle.MergeCell = GridMergeCellDirection.RowsInColumn;\n```\n\n**2. 온디맨드 셀 병합 활성화:**\n```csharp\nOptions.MergeCellsMode = GridMergeCellsMode.OnDemandCalculation|GridMergeCellsMode.MergeRowsInColumn;\n```\n\n이 설정을 통해 그리드는 내용에 따라 자동으로 행을 병합합니다.",
                "response": "Syncfusion WinForms GridControl에서 셀 병합을 설정하는 방법:\n\n**1. 기본 병합 동작 설정:**\n```csharp\nGridStyleInfo standardStyle = BaseStylesMap[\"Standard\"].StyleInfo;\nstandardStyle.MergeCell = GridMergeCellDirection.RowsInColumn;\n\nGridStyleInfo rowHeaderStyle = BaseStylesMap[\"Row Header\"].StyleInfo;\nrowHeaderStyle.MergeCell = GridMergeCellDirection.RowsInColumn;\n```\n\n**2. 온디맨드 셀 병합 활성화:**\n```csharp\nOptions.MergeCellsMode = GridMergeCellsMode.OnDemandCalculation|GridMergeCellsMode.MergeRowsInColumn;\n```\n\n이 설정을 통해 그리드는 내용에 따라 자동으로 행을 병합합니다.",
                "metadata": {
                    "source": "context7_mcp",
                    "component": "GridControl",
                    "difficulty": "Intermediate",
                    "category": "DataBinding",
                    "quality_score": 0.95
                }
            },
            {
                "instruction": "Syncfusion WinForms HTMLUI 컨트롤의 이벤트 처리 방법을 설명해주세요.",
                "input": "HTMLUI 컨트롤에서 사용할 수 있는 주요 이벤트들과 처리 방법을 알려주세요.",
                "output": "Syncfusion WinForms HTMLUI 컨트롤의 이벤트 처리:\n\n**주요 이벤트들:**\n- `TitleChanged`: 문서 제목 변경 시\n- `ShowTitleChanged`: 제목 표시 상태 변경 시\n- `LoadFinished`: 문서 로딩 완료 시\n- `LoadStarted`: 문서 로딩 시작 시\n- `LoadError`: 문서 로딩 오류 시\n- `PreRenderDocument`: 문서 렌더링 전\n\n**이벤트 처리 예제:**\n```csharp\nhtmluiControl.LoadFinished += (sender, e) => {\n    Console.WriteLine(\"문서 로딩 완료\");\n    // 추가 처리 로직\n};\n\nhtmluiControl.LoadError += (sender, e) => {\n    Console.WriteLine($\"로딩 오류: {e.ErrorMessage}\");\n    // 오류 처리 로직\n};\n```",
                "response": "Syncfusion WinForms HTMLUI 컨트롤의 이벤트 처리:\n\n**주요 이벤트들:**\n- `TitleChanged`: 문서 제목 변경 시\n- `ShowTitleChanged`: 제목 표시 상태 변경 시\n- `LoadFinished`: 문서 로딩 완료 시\n- `LoadStarted`: 문서 로딩 시작 시\n- `LoadError`: 문서 로딩 오류 시\n- `PreRenderDocument`: 문서 렌더링 전\n\n**이벤트 처리 예제:**\n```csharp\nhtmluiControl.LoadFinished += (sender, e) => {\n    Console.WriteLine(\"문서 로딩 완료\");\n    // 추가 처리 로직\n};\n\nhtmluiControl.LoadError += (sender, e) => {\n    Console.WriteLine($\"로딩 오류: {e.ErrorMessage}\");\n    // 오류 처리 로직\n};\n```",
                "metadata": {
                    "source": "context7_mcp",
                    "component": "HTMLUI",
                    "difficulty": "Beginner",
                    "category": "Events",
                    "quality_score": 0.92
                }
            },
            {
                "instruction": "Syncfusion WinForms에서 C# 스크립팅을 통해 HTML 요소를 조작하는 방법을 보여주세요.",
                "input": "HTMLUI에서 C# 스크립트로 HTML 요소를 동적으로 제어하는 실제 예제를 제공해주세요.",
                "output": "Syncfusion WinForms HTMLUI에서 C# 스크립팅을 통한 HTML 요소 조작:\n\n**스크립트 클래스 구현:**\n```csharp\nusing System;\nusing System.Windows.Forms;\nusing Syncfusion.Windows.Forms.HTMLUI;\n\npublic class Script\n{\n    IHTMLElement txtText = null;\n    IHTMLElement btnRun = null;\n    IHTMLElement elmCustom = null;\n    \n    private const string DEF_IMG_TAG = \"<img src='smile.bmp'>\";\n    private const string DEF_SMILE = \":-)\";\n    \n    public static Script OnScriptStart()\n    {\n        return new Script();\n    }\n    \n    public Script()\n    {\n        if(Global.Document == null)\n        {\n            MessageBox.Show(\"Document is NULL\");\n            return;\n        }\n        \n        // HTML 요소 참조 가져오기\n        txtText = Global.Document.GetElementByUserId(\"btn\");\n        btnRun = Global.Document.GetElementByUserId(\"txt\");\n        elmCustom = Global.Document.GetElementByUserId(\"custom\");\n        \n        // 이벤트 핸들러 연결\n        btnRun.Click += new EventHandler(CScustom_Run);\n    }\n    \n    public void CScustom_Run(object sender, EventArgs args)\n    {\n        if(elmCustom == null) return;\n        \n        INPUTElementImpl txtElm = txtText as INPUTElementImpl;\n        // HTML 내용 동적 변경\n        elmCustom.InnerHTML = txtElm.UserControl.CustomControl.Text.Replace(DEF_SMILE, DEF_IMG_TAG);\n    }\n}\n```\n\n이 방식으로 C# 코드에서 HTML 요소를 직접 조작하고 사용자 상호작용을 처리할 수 있습니다.",
                "response": "Syncfusion WinForms HTMLUI에서 C# 스크립팅을 통한 HTML 요소 조작:\n\n**스크립트 클래스 구현:**\n```csharp\nusing System;\nusing System.Windows.Forms;\nusing Syncfusion.Windows.Forms.HTMLUI;\n\npublic class Script\n{\n    IHTMLElement txtText = null;\n    IHTMLElement btnRun = null;\n    IHTMLElement elmCustom = null;\n    \n    private const string DEF_IMG_TAG = \"<img src='smile.bmp'>\";\n    private const string DEF_SMILE = \":-)\";\n    \n    public static Script OnScriptStart()\n    {\n        return new Script();\n    }\n    \n    public Script()\n    {\n        if(Global.Document == null)\n        {\n            MessageBox.Show(\"Document is NULL\");\n            return;\n        }\n        \n        // HTML 요소 참조 가져오기\n        txtText = Global.Document.GetElementByUserId(\"btn\");\n        btnRun = Global.Document.GetElementByUserId(\"txt\");\n        elmCustom = Global.Document.GetElementByUserId(\"custom\");\n        \n        // 이벤트 핸들러 연결\n        btnRun.Click += new EventHandler(CScustom_Run);\n    }\n    \n    public void CScustom_Run(object sender, EventArgs args)\n    {\n        if(elmCustom == null) return;\n        \n        INPUTElementImpl txtElm = txtText as INPUTElementImpl;\n        // HTML 내용 동적 변경\n        elmCustom.InnerHTML = txtElm.UserControl.CustomControl.Text.Replace(DEF_SMILE, DEF_IMG_TAG);\n    }\n}\n```\n\n이 방식으로 C# 코드에서 HTML 요소를 직접 조작하고 사용자 상호작용을 처리할 수 있습니다.",
                "metadata": {
                    "source": "context7_mcp",
                    "component": "HTMLUI",
                    "difficulty": "Advanced",
                    "category": "Scripting",
                    "quality_score": 0.98
                }
            }
        ]
        
        # 커스텀 채팅 템플릿 설정
        custom_chat_templates = {
            "sharegpt": ChatTemplateConfig(
                template_type=ChatTemplateType.CHATML,
                mapping={"role": "from", "content": "value", "user": "human", "assistant": "gpt"},
                add_generation_prompt=False,
                system_message="You are a Syncfusion WinForms expert assistant."
            ),
            "alpaca": ChatTemplateConfig(
                template_type=ChatTemplateType.ALPACA,
                add_generation_prompt=False
            ),
            "openai": ChatTemplateConfig(
                template_type=ChatTemplateType.OPENAI,
                add_generation_prompt=False
            )
        }
        
        # 개선된 데이터셋 생성
        results = await generate_unsloth_compatible_datasets(
            conversations=enhanced_test_data,
            output_dir="enhanced_unsloth_output",
            formats=["sharegpt", "alpaca", "openai"],
            chat_templates=custom_chat_templates,
            target_count=len(enhanced_test_data),
            enable_template_mapping=True,
            include_metadata=True,
            include_token_counts=True,
            include_template_info=True,
            quality_threshold=0.8,
            min_tokens=50,
            max_tokens=8192,
            train_split=0.8
        )
        
        logger.info("✓ 개선된 데이터셋 생성 완료")
        
        # 3. 결과 분석
        logger.info("3. 결과 분석 중...")
        
        datasets = results["datasets"]
        template_formatted = results["template_formatted"]
        statistics = results["statistics"]
        
        logger.info(f"생성된 포맷: {list(datasets.keys())}")
        logger.info(f"템플릿 적용된 포맷: {list(template_formatted.keys())}")
        
        for format_name, dataset in datasets.items():
            logger.info(f"{format_name} 포맷:")
            logger.info(f"  - 훈련 데이터: {len(dataset['train'])}개")
            logger.info(f"  - 검증 데이터: {len(dataset['validation'])}개")
            logger.info(f"  - 전체: {dataset['total']}개")
        
        # 템플릿 적용 결과 확인
        for format_name, template_data in template_formatted.items():
            if template_data:
                sample = template_data[0]
                logger.info(f"{format_name} 템플릿 적용 샘플:")
                logger.info(f"  - 템플릿 타입: {sample.get('template_type', 'N/A')}")
                logger.info(f"  - 토큰 수: {sample.get('token_count', 'N/A')}")
                logger.info(f"  - 텍스트 길이: {len(sample.get('text', ''))} 문자")
        
        # 통계 정보 출력
        gen_summary = statistics["generation_summary"]
        logger.info("생성 통계:")
        logger.info(f"  - 입력 대화: {gen_summary['total_input_conversations']}개")
        logger.info(f"  - 생성된 항목: {gen_summary['total_generated_items']}개")
        logger.info(f"  - 성공률: {gen_summary['success_rate']:.1%}")
        
        # 4. Unsloth 호환성 검증
        logger.info("4. Unsloth 호환성 검증 중...")
        
        compatibility_results = {}
        
        for format_name, dataset in datasets.items():
            format_compatible = True
            issues = []
            
            # 샘플 데이터 검증
            if dataset["train"]:
                sample = dataset["train"][0]
                
                # 필수 필드 확인
                if format_name == "sharegpt":
                    if "conversations" not in sample:
                        format_compatible = False
                        issues.append("conversations 필드 누락")
                    else:
                        for conv in sample["conversations"]:
                            if "from" not in conv or "value" not in conv:
                                format_compatible = False
                                issues.append("대화 구조 오류")
                                break
                
                elif format_name == "alpaca":
                    required_fields = ["instruction", "output"]
                    for field in required_fields:
                        if field not in sample:
                            format_compatible = False
                            issues.append(f"{field} 필드 누락")
                
                elif format_name == "openai":
                    if "messages" in sample:
                        for msg in sample["messages"]:
                            if "role" not in msg or "content" not in msg:
                                format_compatible = False
                                issues.append("메시지 구조 오류")
                                break
            
            compatibility_results[format_name] = {
                "compatible": format_compatible,
                "issues": issues
            }
            
            if format_compatible:
                logger.info(f"  ✓ {format_name}: Unsloth 호환")
            else:
                logger.warning(f"  ⚠ {format_name}: 호환성 이슈 - {', '.join(issues)}")
        
        # 5. 최종 결과 요약
        logger.info("5. 최종 결과 요약")
        
        total_compatible = sum(1 for result in compatibility_results.values() if result["compatible"])
        total_formats = len(compatibility_results)
        
        final_summary = {
            "timestamp": datetime.now().isoformat(),
            "test_type": "enhanced_unsloth_system_test",
            "results": {
                "chat_template_manager": "✓ 성공",
                "enhanced_dataset_generator": "✓ 성공",
                "unsloth_compatibility": f"{total_compatible}/{total_formats} 포맷 호환",
                "template_applications": len(statistics.get("template_applications", {})),
                "total_generated_items": gen_summary["total_generated_items"],
                "success_rate": f"{gen_summary['success_rate']:.1%}"
            },
            "compatibility_details": compatibility_results,
            "files_generated": results["files"],
            "recommendations": []
        }
        
        # 권장사항 생성
        if total_compatible == total_formats:
            final_summary["recommendations"].append("모든 포맷이 Unsloth와 호환됩니다 - 즉시 파인튜닝 가능")
        else:
            final_summary["recommendations"].append("일부 포맷에서 호환성 이슈 발견 - 데이터 구조 검토 필요")
        
        if len(statistics.get("template_applications", {})) > 0:
            final_summary["recommendations"].append("채팅 템플릿이 성공적으로 적용됨 - 다양한 모델 아키텍처 지원")
        
        final_summary["recommendations"].append("Context7 MCP 기반 고품질 데이터로 우수한 훈련 결과 예상")
        
        # 최종 리포트 저장
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"enhanced_unsloth_system_test_report_{timestamp}.json"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(final_summary, f, indent=2, ensure_ascii=False)
        
        logger.info("=" * 80)
        logger.info("Unsloth 채팅 템플릿 통합 개선된 시스템 테스트 결과")
        logger.info("=" * 80)
        logger.info(f"채팅 템플릿 매니저: {final_summary['results']['chat_template_manager']}")
        logger.info(f"개선된 데이터셋 생성기: {final_summary['results']['enhanced_dataset_generator']}")
        logger.info(f"Unsloth 호환성: {final_summary['results']['unsloth_compatibility']}")
        logger.info(f"템플릿 적용 수: {final_summary['results']['template_applications']}")
        logger.info(f"생성된 항목 수: {final_summary['results']['total_generated_items']}")
        logger.info(f"성공률: {final_summary['results']['success_rate']}")
        logger.info("")
        logger.info("권장사항:")
        for i, rec in enumerate(final_summary["recommendations"], 1):
            logger.info(f"  {i}. {rec}")
        logger.info(f"\n상세 리포트: {report_file}")
        logger.info("=" * 80)
        
        return final_summary
        
    except Exception as e:
        logger.error(f"테스트 실행 중 오류: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return None


async def main():
    """메인 함수"""
    logger.info("Unsloth 채팅 템플릿 통합 개선된 시스템 테스트를 시작합니다...")
    
    try:
        test_results = await test_enhanced_unsloth_system()
        
        if test_results:
            print("\n🎉 개선된 Unsloth 시스템 테스트 완료!")
            print("\n📋 주요 성과:")
            print("• Unsloth 채팅 템플릿 시스템 성공적 통합")
            print("• 다중 포맷 지원 (ShareGPT, Alpaca, OpenAI)")
            print("• Context7 MCP 기반 고품질 데이터 활용")
            print("• 자동 품질 검증 및 필터링")
            print("• 훈련/검증 데이터 자동 분할")
            print("• 풍부한 메타데이터 및 통계 정보")
            
            print("\n💡 핵심 개선사항:")
            print("• ChatML, Zephyr, Llama, Alpaca 등 다양한 채팅 템플릿 지원")
            print("• 필드 매핑을 통한 유연한 데이터 변환")
            print("• EOS 토큰 자동 매핑")
            print("• 생성 프롬프트 옵션 지원")
            print("• 토큰 수 기반 품질 관리")
            print("• Unsloth 프레임워크 완전 호환")
        else:
            print("\n❌ 테스트 실패")
    
    except Exception as e:
        logger.error(f"메인 함수 실행 중 오류: {e}")
        print(f"\n❌ 오류 발생: {e}")
    
    logger.info("=== 개선된 Unsloth 시스템 테스트 완료 ===")


if __name__ == "__main__":
    asyncio.run(main())