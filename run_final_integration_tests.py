#!/usr/bin/env python3
"""
최종 통합 테스트 실행기
모든 통합 테스트를 순차적으로 실행하고 종합 리포트 생성
"""

import asyncio
import json
import logging
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class FinalIntegrationTestRunner:
    """최종 통합 테스트 실행기"""
    
    def __init__(self):
        self.test_results = {}
        self.start_time = None
        self.end_time = None
        self.test_modules = [
            "test_complete_pipeline_integration",
            "test_performance_validation", 
            "test_unsloth_compatibility"
        ]
    
    async def run_all_tests(self) -> Dict[str, Any]:
        """모든 테스트 실행"""
        logger.info("=" * 80)
        logger.info("최종 통합 테스트 실행 시작")
        logger.info("=" * 80)
        
        self.start_time = datetime.now()
        
        try:
            # 1. 전체 파이프라인 통합 테스트
            await self._run_pipeline_integration_test()
            
            # 2. 성능 검증 테스트
            await self._run_performance_validation_test()
            
            # 3. Unsloth 호환성 테스트
            await self._run_unsloth_compatibility_test()
            
            self.end_time = datetime.now()
            
            # 4. 종합 리포트 생성
            return await self._generate_comprehensive_report()
            
        except Exception as e:
            logger.error(f"테스트 실행 중 치명적 오류: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return {"status": "failed", "error": str(e)}
    
    async def _run_pipeline_integration_test(self):
        """전체 파이프라인 통합 테스트 실행"""
        logger.info("1. 전체 파이프라인 통합 테스트 실행 중...")
        
        test_result = {
            "status": "not_run",
            "start_time": datetime.now().isoformat(),
            "duration": 0,
            "report_file": None,
            "error": None
        }
        
        try:
            start_time = time.time()
            
            # 테스트 모듈 동적 임포트 및 실행
            try:
                from test_complete_pipeline_integration import CompletePipelineIntegrationTest
                
                tester = CompletePipelineIntegrationTest()
                result = await tester.run_complete_test()
                
                test_result["status"] = result.get("status", "unknown")
                test_result["detailed_results"] = result
                
                # 리포트 파일 찾기
                report_files = list(Path(".").glob("complete_pipeline_integration_report_*.json"))
                if report_files:
                    test_result["report_file"] = str(report_files[-1])  # 가장 최근 파일
                
                logger.info("  ✓ 전체 파이프라인 통합 테스트 완료")
                
            except ImportError as e:
                logger.warning(f"  ⚠ 파이프라인 통합 테스트 모듈 없음: {e}")
                test_result["status"] = "skipped"
                test_result["error"] = f"Module not found: {e}"
            
            end_time = time.time()
            test_result["duration"] = end_time - start_time
            
        except Exception as e:
            test_result["status"] = "failed"
            test_result["error"] = str(e)
            logger.error(f"  ✗ 파이프라인 통합 테스트 실패: {e}")
        
        self.test_results["pipeline_integration"] = test_result
    
    async def _run_performance_validation_test(self):
        """성능 검증 테스트 실행"""
        logger.info("2. 성능 검증 테스트 실행 중...")
        
        test_result = {
            "status": "not_run",
            "start_time": datetime.now().isoformat(),
            "duration": 0,
            "report_file": None,
            "error": None
        }
        
        try:
            start_time = time.time()
            
            try:
                from test_performance_validation import PerformanceValidationTest
                
                tester = PerformanceValidationTest()
                result = await tester.run_performance_tests()
                
                test_result["status"] = "success" if result.get("overall_score", 0) > 0 else "failed"
                test_result["detailed_results"] = result
                
                # 리포트 파일 찾기
                report_files = list(Path(".").glob("performance_validation_report_*.json"))
                if report_files:
                    test_result["report_file"] = str(report_files[-1])
                
                logger.info("  ✓ 성능 검증 테스트 완료")
                
            except ImportError as e:
                logger.warning(f"  ⚠ 성능 검증 테스트 모듈 없음: {e}")
                test_result["status"] = "skipped"
                test_result["error"] = f"Module not found: {e}"
            
            end_time = time.time()
            test_result["duration"] = end_time - start_time
            
        except Exception as e:
            test_result["status"] = "failed"
            test_result["error"] = str(e)
            logger.error(f"  ✗ 성능 검증 테스트 실패: {e}")
        
        self.test_results["performance_validation"] = test_result
    
    async def _run_unsloth_compatibility_test(self):
        """Unsloth 호환성 테스트 실행"""
        logger.info("3. Unsloth 호환성 테스트 실행 중...")
        
        test_result = {
            "status": "not_run",
            "start_time": datetime.now().isoformat(),
            "duration": 0,
            "report_file": None,
            "error": None
        }
        
        try:
            start_time = time.time()
            
            try:
                from test_unsloth_compatibility import UnslothCompatibilityTest
                
                tester = UnslothCompatibilityTest()
                result = await tester.run_compatibility_tests()
                
                test_result["status"] = "success" if result.get("overall_score", 0) > 0 else "failed"
                test_result["detailed_results"] = result
                
                # 리포트 파일 찾기
                report_files = list(Path(".").glob("unsloth_compatibility_report_*.json"))
                if report_files:
                    test_result["report_file"] = str(report_files[-1])
                
                logger.info("  ✓ Unsloth 호환성 테스트 완료")
                
            except ImportError as e:
                logger.warning(f"  ⚠ Unsloth 호환성 테스트 모듈 없음: {e}")
                test_result["status"] = "skipped"
                test_result["error"] = f"Module not found: {e}"
            
            end_time = time.time()
            test_result["duration"] = end_time - start_time
            
        except Exception as e:
            test_result["status"] = "failed"
            test_result["error"] = str(e)
            logger.error(f"  ✗ Unsloth 호환성 테스트 실패: {e}")
        
        self.test_results["unsloth_compatibility"] = test_result
    
    async def _generate_comprehensive_report(self) -> Dict[str, Any]:
        """종합 리포트 생성"""
        logger.info("4. 종합 리포트 생성 중...")
        
        total_duration = (self.end_time - self.start_time).total_seconds()
        
        # 테스트 결과 요약
        test_summary = {
            "total_tests": len(self.test_results),
            "passed": 0,
            "failed": 0,
            "skipped": 0,
            "total_duration": total_duration
        }
        
        for test_name, result in self.test_results.items():
            status = result.get("status", "unknown")
            if status == "success":
                test_summary["passed"] += 1
            elif status == "failed":
                test_summary["failed"] += 1
            elif status == "skipped":
                test_summary["skipped"] += 1
        
        # 성능 메트릭 수집
        performance_metrics = {}
        if "performance_validation" in self.test_results:
            perf_result = self.test_results["performance_validation"].get("detailed_results", {})
            performance_metrics = {
                "overall_score": perf_result.get("overall_score", 0),
                "performance_grade": perf_result.get("performance_grade", "N/A"),
                "max_throughput": perf_result.get("summary", {}).get("max_throughput_docs_per_sec", 0),
                "memory_efficiency": perf_result.get("summary", {}).get("memory_efficiency_kb_per_item", 0),
                "scalability_stability": perf_result.get("summary", {}).get("scalability_stability", 0)
            }
        
        # 호환성 메트릭 수집
        compatibility_metrics = {}
        if "unsloth_compatibility" in self.test_results:
            compat_result = self.test_results["unsloth_compatibility"].get("detailed_results", {})
            compatibility_metrics = {
                "overall_score": compat_result.get("overall_score", 0),
                "compatibility_grade": compat_result.get("compatibility_grade", "N/A"),
                "ready_for_training": compat_result.get("summary", {}).get("ready_for_training", False),
                "data_structure_valid": compat_result.get("summary", {}).get("data_structure_valid", False),
                "format_compliant": compat_result.get("summary", {}).get("format_compliant", False)
            }
        
        # 파이프라인 메트릭 수집
        pipeline_metrics = {}
        if "pipeline_integration" in self.test_results:
            pipeline_result = self.test_results["pipeline_integration"].get("detailed_results", {})
            if isinstance(pipeline_result, dict):
                pipeline_metrics = {
                    "status": pipeline_result.get("status", "unknown"),
                    "modules_tested": len(pipeline_result.get("detailed_results", {})),
                    "environment_ready": pipeline_result.get("detailed_results", {}).get("environment_setup", {}).get("status") == "success"
                }
        
        # 전체 시스템 준비도 평가
        system_readiness = self._evaluate_system_readiness(
            test_summary, performance_metrics, compatibility_metrics, pipeline_metrics
        )
        
        # 권장사항 생성
        recommendations = self._generate_comprehensive_recommendations(
            test_summary, performance_metrics, compatibility_metrics, pipeline_metrics
        )
        
        # 종합 리포트 구성
        comprehensive_report = {
            "test_info": {
                "timestamp": self.start_time.isoformat(),
                "total_duration_seconds": total_duration,
                "test_type": "final_integration_comprehensive",
                "test_modules": self.test_modules
            },
            "summary": test_summary,
            "system_readiness": system_readiness,
            "performance_metrics": performance_metrics,
            "compatibility_metrics": compatibility_metrics,
            "pipeline_metrics": pipeline_metrics,
            "detailed_test_results": self.test_results,
            "recommendations": recommendations,
            "report_files": self._collect_report_files()
        }
        
        # 리포트 파일 저장
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"final_integration_comprehensive_report_{timestamp}.json"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(comprehensive_report, f, indent=2, ensure_ascii=False)
        
        # 결과 출력
        self._print_comprehensive_results(comprehensive_report, report_file)
        
        return comprehensive_report
    
    def _evaluate_system_readiness(self, test_summary, performance_metrics, compatibility_metrics, pipeline_metrics) -> Dict[str, Any]:
        """시스템 준비도 평가"""
        
        # 기본 점수 계산
        test_success_rate = test_summary["passed"] / test_summary["total_tests"] if test_summary["total_tests"] > 0 else 0
        performance_score = performance_metrics.get("overall_score", 0) / 100
        compatibility_score = compatibility_metrics.get("overall_score", 0) / 100
        
        # 가중 평균 계산
        weights = {
            "test_success": 0.3,
            "performance": 0.35,
            "compatibility": 0.35
        }
        
        overall_readiness = (
            test_success_rate * weights["test_success"] +
            performance_score * weights["performance"] +
            compatibility_score * weights["compatibility"]
        ) * 100
        
        # 준비도 등급 결정
        if overall_readiness >= 95:
            readiness_grade = "Production Ready"
        elif overall_readiness >= 90:
            readiness_grade = "Near Production Ready"
        elif overall_readiness >= 80:
            readiness_grade = "Development Ready"
        elif overall_readiness >= 70:
            readiness_grade = "Testing Ready"
        elif overall_readiness >= 60:
            readiness_grade = "Basic Functionality"
        else:
            readiness_grade = "Not Ready"
        
        # 개별 준비도 체크
        readiness_checks = {
            "tests_passing": test_summary["failed"] == 0,
            "performance_acceptable": performance_metrics.get("overall_score", 0) >= 70,
            "compatibility_verified": compatibility_metrics.get("ready_for_training", False),
            "pipeline_functional": pipeline_metrics.get("status") == "success",
            "environment_configured": pipeline_metrics.get("environment_ready", False)
        }
        
        return {
            "overall_score": overall_readiness,
            "readiness_grade": readiness_grade,
            "individual_checks": readiness_checks,
            "critical_issues": test_summary["failed"] > 0,
            "performance_issues": performance_metrics.get("overall_score", 0) < 70,
            "compatibility_issues": not compatibility_metrics.get("ready_for_training", False)
        }
    
    def _generate_comprehensive_recommendations(self, test_summary, performance_metrics, compatibility_metrics, pipeline_metrics) -> List[str]:
        """종합 권장사항 생성"""
        recommendations = []
        
        # 테스트 실패 관련
        if test_summary["failed"] > 0:
            recommendations.append(f"실패한 테스트 {test_summary['failed']}개 해결 필요 - 상세 로그 확인")
        
        # 성능 관련
        perf_score = performance_metrics.get("overall_score", 0)
        if perf_score < 70:
            recommendations.append(f"성능 개선 필요 (현재: {perf_score:.1f}/100) - 처리량 및 메모리 최적화")
        elif perf_score < 85:
            recommendations.append("성능 최적화 권장 - 더 나은 사용자 경험을 위해")
        
        # 호환성 관련
        compat_score = compatibility_metrics.get("overall_score", 0)
        if not compatibility_metrics.get("ready_for_training", False):
            recommendations.append("Unsloth 호환성 이슈 해결 필요 - 데이터 포맷 및 구조 검토")
        elif compat_score < 90:
            recommendations.append("호환성 개선 권장 - 더 안정적인 훈련을 위해")
        
        # 파이프라인 관련
        if pipeline_metrics.get("status") != "success":
            recommendations.append("파이프라인 통합 이슈 해결 필요 - 모듈 간 연동 확인")
        
        if not pipeline_metrics.get("environment_ready", False):
            recommendations.append("환경 설정 완료 필요 - 필수 모듈 및 설정 파일 확인")
        
        # 전체적인 권장사항
        if not recommendations:
            recommendations.append("모든 테스트 통과 - 프로덕션 배포 준비 완료")
            recommendations.append("정기적인 성능 모니터링 및 품질 검증 권장")
        else:
            recommendations.append("이슈 해결 후 재테스트 실행 권장")
        
        return recommendations
    
    def _collect_report_files(self) -> Dict[str, str]:
        """생성된 리포트 파일들 수집"""
        report_files = {}
        
        for test_name, result in self.test_results.items():
            report_file = result.get("report_file")
            if report_file and Path(report_file).exists():
                report_files[test_name] = report_file
        
        return report_files
    
    def _print_comprehensive_results(self, report: Dict[str, Any], report_file: str):
        """종합 결과 출력"""
        logger.info("=" * 80)
        logger.info("최종 통합 테스트 종합 결과")
        logger.info("=" * 80)
        
        # 기본 정보
        summary = report["summary"]
        readiness = report["system_readiness"]
        
        logger.info(f"총 테스트 시간: {summary['total_duration']:.1f}초")
        logger.info(f"테스트 결과: {summary['passed']}개 성공, {summary['failed']}개 실패, {summary['skipped']}개 건너뜀")
        logger.info(f"시스템 준비도: {readiness['overall_score']:.1f}/100 ({readiness['readiness_grade']})")
        
        # 성능 메트릭
        perf = report["performance_metrics"]
        if perf:
            logger.info(f"성능 점수: {perf.get('overall_score', 0):.1f}/100 (등급: {perf.get('performance_grade', 'N/A')})")
            logger.info(f"최대 처리량: {perf.get('max_throughput', 0):.1f} docs/sec")
        
        # 호환성 메트릭
        compat = report["compatibility_metrics"]
        if compat:
            logger.info(f"호환성 점수: {compat.get('overall_score', 0):.1f}/100 (등급: {compat.get('compatibility_grade', 'N/A')})")
            logger.info(f"Unsloth 훈련 준비: {'완료' if compat.get('ready_for_training', False) else '미완료'}")
        
        # 준비도 체크
        logger.info("")
        logger.info("시스템 준비도 체크:")
        checks = readiness["individual_checks"]
        for check_name, status in checks.items():
            status_icon = "✓" if status else "✗"
            check_display = check_name.replace("_", " ").title()
            logger.info(f"  {status_icon} {check_display}")
        
        # 권장사항
        logger.info("")
        logger.info("권장사항:")
        for i, rec in enumerate(report["recommendations"], 1):
            logger.info(f"  {i}. {rec}")
        
        # 리포트 파일들
        logger.info("")
        logger.info("생성된 리포트 파일:")
        logger.info(f"  종합 리포트: {report_file}")
        for test_name, file_path in report["report_files"].items():
            logger.info(f"  {test_name}: {file_path}")
        
        logger.info("=" * 80)


async def main():
    """메인 함수"""
    print("최종 통합 테스트를 시작합니다...")
    print("이 테스트는 전체 시스템의 준비도를 종합적으로 평가합니다.")
    print("테스트 완료까지 수 분이 소요될 수 있습니다.\n")
    
    runner = FinalIntegrationTestRunner()
    
    try:
        comprehensive_report = await runner.run_all_tests()
        
        readiness = comprehensive_report.get("system_readiness", {})
        overall_score = readiness.get("overall_score", 0)
        grade = readiness.get("readiness_grade", "Unknown")
        
        if overall_score >= 90:
            print(f"\n🎉 최종 통합 테스트 완료! 시스템 준비도: {overall_score:.1f}/100")
            print(f"상태: {grade}")
            print("시스템이 프로덕션 환경에서 사용할 준비가 되었습니다!")
        elif overall_score >= 70:
            print(f"\n✅ 최종 통합 테스트 완료! 시스템 준비도: {overall_score:.1f}/100")
            print(f"상태: {grade}")
            print("시스템이 기본적인 기능을 수행할 준비가 되었습니다.")
        else:
            print(f"\n⚠️ 최종 통합 테스트 완료! 시스템 준비도: {overall_score:.1f}/100")
            print(f"상태: {grade}")
            print("시스템 개선이 필요합니다.")
        
        # 중요한 이슈 알림
        if readiness.get("critical_issues", False):
            print("\n🚨 중요: 실패한 테스트가 있습니다. 상세 로그를 확인해주세요.")
        
        if readiness.get("compatibility_issues", False):
            print("\n⚠️ 주의: Unsloth 호환성 이슈가 있습니다. 데이터 포맷을 확인해주세요.")
        
    except KeyboardInterrupt:
        print("\n\n테스트가 사용자에 의해 중단되었습니다.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"최종 통합 테스트 실행 중 오류 발생: {e}")
        print(f"\n❌ 최종 통합 테스트 실패: {e}")
        sys.exit(1)
    
    print("\n=== 최종 통합 테스트 완료 ===")


if __name__ == "__main__":
    asyncio.run(main())