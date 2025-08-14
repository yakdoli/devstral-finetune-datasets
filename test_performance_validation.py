#!/usr/bin/env python3
"""
성능 검증 테스트
대용량 데이터셋 처리 성능 및 확장성 테스트
"""

import asyncio
import json
import logging
import time
import psutil
import gc
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any
from concurrent.futures import ThreadPoolExecutor

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class PerformanceValidationTest:
    """성능 검증 테스트 클래스"""
    
    def __init__(self):
        self.performance_metrics = {}
        self.baseline_metrics = {}
        self.test_results = {}
    
    async def run_performance_tests(self) -> Dict[str, Any]:
        """성능 테스트 실행"""
        logger.info("=== 성능 검증 테스트 시작 ===")
        
        try:
            # 1. 기준 성능 측정
            await self._measure_baseline_performance()
            
            # 2. 처리량 테스트
            await self._test_throughput_performance()
            
            # 3. 메모리 사용량 테스트
            await self._test_memory_performance()
            
            # 4. 동시성 테스트
            await self._test_concurrency_performance()
            
            # 5. 확장성 테스트
            await self._test_scalability()
            
            # 6. 스트레스 테스트
            await self._test_stress_performance()
            
            # 7. 최종 성능 리포트 생성
            return await self._generate_performance_report()
            
        except Exception as e:
            logger.error(f"성능 테스트 실행 중 오류: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return {"status": "failed", "error": str(e)}
    
    async def _measure_baseline_performance(self):
        """기준 성능 측정"""
        logger.info("1. 기준 성능 측정 중...")
        
        process = psutil.Process()
        
        # 시스템 리소스 기준 측정
        baseline = {
            "cpu_count": psutil.cpu_count(),
            "memory_total_gb": psutil.virtual_memory().total / (1024**3),
            "memory_available_gb": psutil.virtual_memory().available / (1024**3),
            "initial_memory_mb": process.memory_info().rss / (1024**2),
            "initial_cpu_percent": process.cpu_percent(interval=1)
        }
        
        self.baseline_metrics = baseline
        
        logger.info(f"  CPU 코어: {baseline['cpu_count']}개")
        logger.info(f"  총 메모리: {baseline['memory_total_gb']:.1f}GB")
        logger.info(f"  사용 가능 메모리: {baseline['memory_available_gb']:.1f}GB")
        logger.info(f"  초기 프로세스 메모리: {baseline['initial_memory_mb']:.1f}MB")
        logger.info("✓ 기준 성능 측정 완료")
    
    async def _test_throughput_performance(self):
        """처리량 성능 테스트"""
        logger.info("2. 처리량 성능 테스트 중...")
        
        test_result = {
            "batch_performance": {},
            "document_processing": {},
            "conversation_generation": {}
        }
        
        # 배치 크기별 성능 테스트
        batch_sizes = [1, 5, 10, 20, 50]
        
        for batch_size in batch_sizes:
            logger.info(f"  배치 크기 {batch_size} 테스트 중...")
            
            # 테스트 데이터 생성
            test_documents = [
                {
                    "id": f"perf_doc_{i}",
                    "content": f"Performance test document {i} " * 50,  # 긴 콘텐츠
                    "component": f"TestComponent{i % 5}",
                    "metadata": {"test": True, "batch_size": batch_size}
                }
                for i in range(batch_size)
            ]
            
            # 처리 시간 측정
            start_time = time.time()
            start_memory = psutil.Process().memory_info().rss / (1024**2)
            
            # 문서 처리 시뮬레이션
            processed_docs = []
            for doc in test_documents:
                # 실제 처리 로직 시뮬레이션
                await asyncio.sleep(0.01)  # 처리 시간 시뮬레이션
                processed_doc = {
                    **doc,
                    "processed": True,
                    "processing_timestamp": datetime.now().isoformat(),
                    "word_count": len(doc["content"].split())
                }
                processed_docs.append(processed_doc)
            
            end_time = time.time()
            end_memory = psutil.Process().memory_info().rss / (1024**2)
            
            processing_time = end_time - start_time
            memory_increase = end_memory - start_memory
            throughput = len(test_documents) / processing_time
            
            test_result["batch_performance"][batch_size] = {
                "documents": len(test_documents),
                "processing_time": processing_time,
                "throughput_docs_per_sec": throughput,
                "memory_increase_mb": memory_increase,
                "avg_time_per_doc": processing_time / len(test_documents)
            }
            
            logger.info(f"    처리량: {throughput:.2f} docs/sec")
            logger.info(f"    메모리 증가: {memory_increase:.1f}MB")
        
        self.test_results["throughput"] = test_result
        logger.info("✓ 처리량 성능 테스트 완료")  
  async def _test_memory_performance(self):
        """메모리 사용량 성능 테스트"""
        logger.info("3. 메모리 사용량 성능 테스트 중...")
        
        test_result = {
            "memory_scaling": {},
            "memory_leaks": {},
            "garbage_collection": {}
        }
        
        process = psutil.Process()
        initial_memory = process.memory_info().rss / (1024**2)
        
        # 데이터 크기별 메모리 사용량 테스트
        data_sizes = [100, 500, 1000, 2000]
        
        for data_size in data_sizes:
            logger.info(f"  데이터 크기 {data_size} 테스트 중...")
            
            gc.collect()  # 가비지 컬렉션 실행
            before_memory = process.memory_info().rss / (1024**2)
            
            # 대용량 데이터 생성
            large_dataset = []
            for i in range(data_size):
                large_item = {
                    "id": f"large_item_{i}",
                    "content": "Large content data " * 100,  # 큰 콘텐츠
                    "metadata": {
                        "index": i,
                        "timestamp": datetime.now().isoformat(),
                        "large_field": "x" * 1000  # 1KB 문자열
                    },
                    "conversations": [
                        {"from": "human", "value": f"Question {i}"},
                        {"from": "gpt", "value": f"Answer {i} with detailed explanation " * 20}
                    ]
                }
                large_dataset.append(large_item)
            
            after_creation = process.memory_info().rss / (1024**2)
            
            # 데이터 처리 시뮬레이션
            processed_items = 0
            for item in large_dataset:
                # 처리 시뮬레이션
                item["processed"] = True
                processed_items += 1
                
                # 중간 메모리 체크
                if processed_items % 500 == 0:
                    current_memory = process.memory_info().rss / (1024**2)
                    logger.debug(f"    처리 중 메모리: {current_memory:.1f}MB")
            
            after_processing = process.memory_info().rss / (1024**2)
            
            # 데이터 삭제 후 메모리 확인
            del large_dataset
            gc.collect()
            after_cleanup = process.memory_info().rss / (1024**2)
            
            test_result["memory_scaling"][data_size] = {
                "initial_memory_mb": before_memory,
                "after_creation_mb": after_creation,
                "after_processing_mb": after_processing,
                "after_cleanup_mb": after_cleanup,
                "creation_increase_mb": after_creation - before_memory,
                "processing_increase_mb": after_processing - after_creation,
                "cleanup_decrease_mb": after_processing - after_cleanup,
                "memory_per_item_kb": (after_creation - before_memory) * 1024 / data_size
            }
            
            logger.info(f"    메모리 증가: {after_creation - before_memory:.1f}MB")
            logger.info(f"    항목당 메모리: {(after_creation - before_memory) * 1024 / data_size:.2f}KB")
        
        # 메모리 누수 테스트
        logger.info("  메모리 누수 테스트 중...")
        
        leak_test_iterations = 10
        memory_samples = []
        
        for iteration in range(leak_test_iterations):
            # 반복적인 데이터 생성 및 삭제
            temp_data = [{"data": "x" * 1000} for _ in range(100)]
            
            # 처리 시뮬레이션
            for item in temp_data:
                item["processed"] = True
            
            # 메모리 측정
            current_memory = process.memory_info().rss / (1024**2)
            memory_samples.append(current_memory)
            
            # 데이터 삭제
            del temp_data
            gc.collect()
            
            await asyncio.sleep(0.1)  # 짧은 대기
        
        # 메모리 누수 분석
        memory_trend = []
        for i in range(1, len(memory_samples)):
            trend = memory_samples[i] - memory_samples[i-1]
            memory_trend.append(trend)
        
        avg_memory_increase = sum(memory_trend) / len(memory_trend)
        
        test_result["memory_leaks"] = {
            "iterations": leak_test_iterations,
            "memory_samples": memory_samples,
            "avg_increase_per_iteration": avg_memory_increase,
            "total_increase": memory_samples[-1] - memory_samples[0],
            "potential_leak": avg_memory_increase > 0.5  # 0.5MB 이상 증가시 누수 의심
        }
        
        if test_result["memory_leaks"]["potential_leak"]:
            logger.warning(f"  ⚠ 메모리 누수 의심: 평균 {avg_memory_increase:.2f}MB/iteration 증가")
        else:
            logger.info("  ✓ 메모리 누수 없음")
        
        self.test_results["memory"] = test_result
        logger.info("✓ 메모리 성능 테스트 완료")
    
    async def _test_concurrency_performance(self):
        """동시성 성능 테스트"""
        logger.info("4. 동시성 성능 테스트 중...")
        
        test_result = {
            "concurrent_processing": {},
            "async_performance": {},
            "thread_performance": {}
        }
        
        # 동시 처리 수준별 테스트
        concurrency_levels = [1, 2, 4, 8, 16]
        
        for concurrency in concurrency_levels:
            logger.info(f"  동시성 레벨 {concurrency} 테스트 중...")
            
            # 비동기 처리 테스트
            async def async_task(task_id: int):
                start_time = time.time()
                
                # 작업 시뮬레이션
                await asyncio.sleep(0.1)  # I/O 대기 시뮬레이션
                
                # CPU 집약적 작업 시뮬레이션
                result = sum(i * i for i in range(1000))
                
                end_time = time.time()
                return {
                    "task_id": task_id,
                    "processing_time": end_time - start_time,
                    "result": result
                }
            
            # 비동기 작업 실행
            start_time = time.time()
            
            tasks = [async_task(i) for i in range(concurrency)]
            async_results = await asyncio.gather(*tasks)
            
            async_end_time = time.time()
            async_total_time = async_end_time - start_time
            
            # 스레드 풀 처리 테스트
            def sync_task(task_id: int):
                start_time = time.time()
                
                # CPU 집약적 작업
                result = sum(i * i for i in range(1000))
                time.sleep(0.1)  # 블로킹 작업 시뮬레이션
                
                end_time = time.time()
                return {
                    "task_id": task_id,
                    "processing_time": end_time - start_time,
                    "result": result
                }
            
            # 스레드 풀 실행
            thread_start_time = time.time()
            
            with ThreadPoolExecutor(max_workers=concurrency) as executor:
                thread_futures = [executor.submit(sync_task, i) for i in range(concurrency)]
                thread_results = [future.result() for future in thread_futures]
            
            thread_end_time = time.time()
            thread_total_time = thread_end_time - thread_start_time
            
            # 결과 분석
            async_avg_time = sum(r["processing_time"] for r in async_results) / len(async_results)
            thread_avg_time = sum(r["processing_time"] for r in thread_results) / len(thread_results)
            
            test_result["concurrent_processing"][concurrency] = {
                "async_total_time": async_total_time,
                "async_avg_task_time": async_avg_time,
                "async_efficiency": concurrency / async_total_time,
                "thread_total_time": thread_total_time,
                "thread_avg_task_time": thread_avg_time,
                "thread_efficiency": concurrency / thread_total_time,
                "async_vs_thread_ratio": async_total_time / thread_total_time
            }
            
            logger.info(f"    비동기: {async_total_time:.2f}초")
            logger.info(f"    스레드: {thread_total_time:.2f}초")
            logger.info(f"    효율성 비율: {async_total_time / thread_total_time:.2f}")
        
        self.test_results["concurrency"] = test_result
        logger.info("✓ 동시성 성능 테스트 완료")  
  async def _test_scalability(self):
        """확장성 테스트"""
        logger.info("5. 확장성 테스트 중...")
        
        test_result = {
            "data_scaling": {},
            "user_scaling": {},
            "resource_scaling": {}
        }
        
        # 데이터 크기 확장성 테스트
        data_scales = [100, 500, 1000, 2500, 5000]
        
        for scale in data_scales:
            logger.info(f"  데이터 규모 {scale} 테스트 중...")
            
            start_time = time.time()
            start_memory = psutil.Process().memory_info().rss / (1024**2)
            
            # 대규모 데이터 처리 시뮬레이션
            processed_count = 0
            batch_size = min(100, scale // 10)  # 동적 배치 크기
            
            for batch_start in range(0, scale, batch_size):
                batch_end = min(batch_start + batch_size, scale)
                batch_data = []
                
                # 배치 데이터 생성
                for i in range(batch_start, batch_end):
                    item = {
                        "id": f"scale_test_{i}",
                        "content": f"Scalability test content {i}",
                        "metadata": {"batch": batch_start // batch_size}
                    }
                    batch_data.append(item)
                
                # 배치 처리 시뮬레이션
                for item in batch_data:
                    item["processed"] = True
                    processed_count += 1
                
                # 메모리 정리
                if batch_start % (batch_size * 10) == 0:
                    gc.collect()
                
                await asyncio.sleep(0.001)  # 짧은 대기
            
            end_time = time.time()
            end_memory = psutil.Process().memory_info().rss / (1024**2)
            
            processing_time = end_time - start_time
            memory_increase = end_memory - start_memory
            throughput = processed_count / processing_time
            
            test_result["data_scaling"][scale] = {
                "processed_items": processed_count,
                "processing_time": processing_time,
                "throughput": throughput,
                "memory_increase_mb": memory_increase,
                "time_per_item_ms": (processing_time * 1000) / processed_count,
                "memory_per_item_kb": (memory_increase * 1024) / processed_count if memory_increase > 0 else 0
            }
            
            logger.info(f"    처리량: {throughput:.1f} items/sec")
            logger.info(f"    항목당 시간: {(processing_time * 1000) / processed_count:.2f}ms")
        
        # 확장성 분석
        scales = list(test_result["data_scaling"].keys())
        throughputs = [test_result["data_scaling"][s]["throughput"] for s in scales]
        
        # 선형 확장성 분석 (이상적으로는 일정한 처리량 유지)
        throughput_variance = max(throughputs) - min(throughputs)
        throughput_stability = 1 - (throughput_variance / max(throughputs))
        
        test_result["scalability_analysis"] = {
            "throughput_variance": throughput_variance,
            "throughput_stability": throughput_stability,
            "scales_tested": scales,
            "max_throughput": max(throughputs),
            "min_throughput": min(throughputs),
            "is_scalable": throughput_stability > 0.7  # 70% 이상 안정성
        }
        
        if test_result["scalability_analysis"]["is_scalable"]:
            logger.info(f"  ✓ 확장성 양호 (안정성: {throughput_stability:.1%})")
        else:
            logger.warning(f"  ⚠ 확장성 이슈 (안정성: {throughput_stability:.1%})")
        
        self.test_results["scalability"] = test_result
        logger.info("✓ 확장성 테스트 완료")
    
    async def _test_stress_performance(self):
        """스트레스 테스트"""
        logger.info("6. 스트레스 테스트 중...")
        
        test_result = {
            "high_load": {},
            "resource_limits": {},
            "recovery_test": {}
        }
        
        process = psutil.Process()
        
        # 고부하 테스트
        logger.info("  고부하 테스트 중...")
        
        stress_duration = 30  # 30초 스트레스 테스트
        stress_start_time = time.time()
        
        # 동시 작업 생성
        stress_tasks = []
        task_count = 50  # 50개 동시 작업
        
        async def stress_task(task_id: int):
            task_start = time.time()
            iterations = 0
            
            while time.time() - stress_start_time < stress_duration:
                # CPU 집약적 작업
                result = sum(i * i for i in range(100))
                
                # 메모리 사용
                temp_data = [f"stress_data_{i}" for i in range(100)]
                
                # I/O 시뮬레이션
                await asyncio.sleep(0.01)
                
                iterations += 1
                
                # 메모리 정리
                del temp_data
                
                if iterations % 100 == 0:
                    gc.collect()
            
            task_end = time.time()
            return {
                "task_id": task_id,
                "iterations": iterations,
                "duration": task_end - task_start
            }
        
        # 스트레스 작업 실행
        stress_tasks = [stress_task(i) for i in range(task_count)]
        
        # 리소스 모니터링
        resource_samples = []
        monitoring_task = asyncio.create_task(self._monitor_resources_during_stress(stress_duration, resource_samples))
        
        # 스트레스 작업 및 모니터링 실행
        stress_results, _ = await asyncio.gather(
            asyncio.gather(*stress_tasks),
            monitoring_task
        )
        
        stress_end_time = time.time()
        total_stress_time = stress_end_time - stress_start_time
        
        # 스트레스 테스트 결과 분석
        total_iterations = sum(r["iterations"] for r in stress_results)
        avg_iterations = total_iterations / len(stress_results)
        
        test_result["high_load"] = {
            "duration_seconds": total_stress_time,
            "concurrent_tasks": task_count,
            "total_iterations": total_iterations,
            "avg_iterations_per_task": avg_iterations,
            "iterations_per_second": total_iterations / total_stress_time,
            "resource_samples": resource_samples
        }
        
        # 리소스 한계 분석
        if resource_samples:
            max_cpu = max(sample["cpu_percent"] for sample in resource_samples)
            max_memory = max(sample["memory_mb"] for sample in resource_samples)
            avg_cpu = sum(sample["cpu_percent"] for sample in resource_samples) / len(resource_samples)
            avg_memory = sum(sample["memory_mb"] for sample in resource_samples) / len(resource_samples)
            
            test_result["resource_limits"] = {
                "max_cpu_percent": max_cpu,
                "max_memory_mb": max_memory,
                "avg_cpu_percent": avg_cpu,
                "avg_memory_mb": avg_memory,
                "cpu_utilization": avg_cpu / 100,
                "memory_pressure": max_memory > (self.baseline_metrics["memory_available_gb"] * 1024 * 0.8)
            }
            
            logger.info(f"    최대 CPU 사용률: {max_cpu:.1f}%")
            logger.info(f"    최대 메모리 사용량: {max_memory:.1f}MB")
            logger.info(f"    초당 반복 수: {total_iterations / total_stress_time:.1f}")
        
        # 복구 테스트
        logger.info("  시스템 복구 테스트 중...")
        
        recovery_start = time.time()
        
        # 가비지 컬렉션 및 메모리 정리
        gc.collect()
        
        # 복구 후 성능 측정
        recovery_tasks = [self._simple_performance_task(i) for i in range(10)]
        recovery_results = await asyncio.gather(*recovery_tasks)
        
        recovery_end = time.time()
        recovery_time = recovery_end - recovery_start
        
        recovery_avg_time = sum(r["processing_time"] for r in recovery_results) / len(recovery_results)
        
        test_result["recovery_test"] = {
            "recovery_time_seconds": recovery_time,
            "post_stress_avg_task_time": recovery_avg_time,
            "performance_degradation": recovery_avg_time > 0.2,  # 0.2초 이상이면 성능 저하
            "system_recovered": recovery_avg_time < 0.5  # 0.5초 미만이면 복구됨
        }
        
        if test_result["recovery_test"]["system_recovered"]:
            logger.info("  ✓ 시스템 정상 복구")
        else:
            logger.warning("  ⚠ 시스템 복구 지연")
        
        self.test_results["stress"] = test_result
        logger.info("✓ 스트레스 테스트 완료")
    
    async def _monitor_resources_during_stress(self, duration: float, samples: List[Dict]):
        """스트레스 테스트 중 리소스 모니터링"""
        start_time = time.time()
        process = psutil.Process()
        
        while time.time() - start_time < duration:
            sample = {
                "timestamp": time.time() - start_time,
                "cpu_percent": process.cpu_percent(),
                "memory_mb": process.memory_info().rss / (1024**2),
                "system_cpu_percent": psutil.cpu_percent(),
                "system_memory_percent": psutil.virtual_memory().percent
            }
            samples.append(sample)
            
            await asyncio.sleep(0.5)  # 0.5초마다 샘플링
    
    async def _simple_performance_task(self, task_id: int):
        """간단한 성능 측정 작업"""
        start_time = time.time()
        
        # 간단한 작업 수행
        result = sum(i for i in range(1000))
        await asyncio.sleep(0.01)
        
        end_time = time.time()
        
        return {
            "task_id": task_id,
            "processing_time": end_time - start_time,
            "result": result
        }    a
sync def _generate_performance_report(self) -> Dict[str, Any]:
        """성능 리포트 생성"""
        logger.info("7. 성능 리포트 생성 중...")
        
        # 성능 점수 계산
        performance_scores = {}
        
        # 처리량 점수 (높을수록 좋음)
        if "throughput" in self.test_results:
            throughput_data = self.test_results["throughput"]["batch_performance"]
            max_throughput = max(data["throughput_docs_per_sec"] for data in throughput_data.values())
            performance_scores["throughput"] = min(100, max_throughput * 10)  # 10 docs/sec = 100점
        
        # 메모리 효율성 점수 (낮을수록 좋음)
        if "memory" in self.test_results:
            memory_data = self.test_results["memory"]["memory_scaling"]
            avg_memory_per_item = sum(data["memory_per_item_kb"] for data in memory_data.values()) / len(memory_data)
            performance_scores["memory_efficiency"] = max(0, 100 - avg_memory_per_item)  # 1KB/item = 99점
        
        # 동시성 효율성 점수
        if "concurrency" in self.test_results:
            concurrency_data = self.test_results["concurrency"]["concurrent_processing"]
            max_efficiency = max(data["async_efficiency"] for data in concurrency_data.values())
            performance_scores["concurrency"] = min(100, max_efficiency * 10)  # 10 tasks/sec = 100점
        
        # 확장성 점수
        if "scalability" in self.test_results:
            scalability_data = self.test_results["scalability"]["scalability_analysis"]
            stability = scalability_data["throughput_stability"]
            performance_scores["scalability"] = stability * 100
        
        # 스트레스 내성 점수
        if "stress" in self.test_results:
            stress_data = self.test_results["stress"]
            recovery_score = 100 if stress_data["recovery_test"]["system_recovered"] else 50
            resource_score = 100 - min(100, stress_data["resource_limits"]["max_cpu_percent"])
            performance_scores["stress_resistance"] = (recovery_score + resource_score) / 2
        
        # 전체 성능 점수
        overall_score = sum(performance_scores.values()) / len(performance_scores) if performance_scores else 0
        
        # 성능 등급 결정
        if overall_score >= 90:
            performance_grade = "A"
        elif overall_score >= 80:
            performance_grade = "B"
        elif overall_score >= 70:
            performance_grade = "C"
        elif overall_score >= 60:
            performance_grade = "D"
        else:
            performance_grade = "F"
        
        # 권장사항 생성
        recommendations = []
        
        if performance_scores.get("throughput", 0) < 70:
            recommendations.append("처리량 개선을 위해 배치 크기 최적화 필요")
        
        if performance_scores.get("memory_efficiency", 0) < 70:
            recommendations.append("메모리 사용량 최적화 필요 - 데이터 구조 개선 고려")
        
        if performance_scores.get("concurrency", 0) < 70:
            recommendations.append("동시성 처리 개선 필요 - 비동기 처리 최적화")
        
        if performance_scores.get("scalability", 0) < 70:
            recommendations.append("확장성 개선 필요 - 아키텍처 재검토")
        
        if performance_scores.get("stress_resistance", 0) < 70:
            recommendations.append("스트레스 내성 개선 필요 - 리소스 관리 강화")
        
        if not recommendations:
            recommendations.append("모든 성능 지표가 양호함 - 현재 설정 유지")
        
        # 최종 리포트 구성
        performance_report = {
            "test_info": {
                "timestamp": datetime.now().isoformat(),
                "test_type": "performance_validation",
                "baseline_metrics": self.baseline_metrics
            },
            "performance_scores": performance_scores,
            "overall_score": overall_score,
            "performance_grade": performance_grade,
            "detailed_results": self.test_results,
            "recommendations": recommendations,
            "summary": {
                "max_throughput_docs_per_sec": max(
                    data["throughput_docs_per_sec"] 
                    for data in self.test_results.get("throughput", {}).get("batch_performance", {}).values()
                ) if "throughput" in self.test_results else 0,
                "memory_efficiency_kb_per_item": sum(
                    data["memory_per_item_kb"] 
                    for data in self.test_results.get("memory", {}).get("memory_scaling", {}).values()
                ) / len(self.test_results.get("memory", {}).get("memory_scaling", {})) if "memory" in self.test_results else 0,
                "max_concurrent_efficiency": max(
                    data["async_efficiency"] 
                    for data in self.test_results.get("concurrency", {}).get("concurrent_processing", {}).values()
                ) if "concurrency" in self.test_results else 0,
                "scalability_stability": self.test_results.get("scalability", {}).get("scalability_analysis", {}).get("throughput_stability", 0),
                "stress_recovery_success": self.test_results.get("stress", {}).get("recovery_test", {}).get("system_recovered", False)
            }
        }
        
        # 리포트 파일 저장
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"performance_validation_report_{timestamp}.json"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(performance_report, f, indent=2, ensure_ascii=False)
        
        # 결과 출력
        logger.info("=" * 60)
        logger.info("성능 검증 테스트 결과")
        logger.info("=" * 60)
        logger.info(f"전체 성능 점수: {overall_score:.1f}/100 (등급: {performance_grade})")
        logger.info(f"처리량 점수: {performance_scores.get('throughput', 0):.1f}/100")
        logger.info(f"메모리 효율성: {performance_scores.get('memory_efficiency', 0):.1f}/100")
        logger.info(f"동시성 효율성: {performance_scores.get('concurrency', 0):.1f}/100")
        logger.info(f"확장성: {performance_scores.get('scalability', 0):.1f}/100")
        logger.info(f"스트레스 내성: {performance_scores.get('stress_resistance', 0):.1f}/100")
        logger.info("")
        logger.info("권장사항:")
        for i, rec in enumerate(recommendations, 1):
            logger.info(f"  {i}. {rec}")
        logger.info(f"\n상세 리포트: {report_file}")
        logger.info("=" * 60)
        
        return performance_report


async def main():
    """메인 함수"""
    print("성능 검증 테스트를 시작합니다...")
    print("이 테스트는 시스템의 성능 특성을 종합적으로 분석합니다.\n")
    
    tester = PerformanceValidationTest()
    
    try:
        performance_report = await tester.run_performance_tests()
        
        overall_score = performance_report.get("overall_score", 0)
        grade = performance_report.get("performance_grade", "F")
        
        if grade in ["A", "B"]:
            print(f"\n🎉 성능 검증 완료! 전체 점수: {overall_score:.1f}/100 (등급: {grade})")
            print("시스템이 우수한 성능을 보여줍니다.")
        elif grade == "C":
            print(f"\n✅ 성능 검증 완료! 전체 점수: {overall_score:.1f}/100 (등급: {grade})")
            print("시스템 성능이 양호하지만 개선 여지가 있습니다.")
        else:
            print(f"\n⚠️ 성능 검증 완료! 전체 점수: {overall_score:.1f}/100 (등급: {grade})")
            print("성능 개선이 필요합니다.")
        
        # 주요 성능 지표 출력
        summary = performance_report.get("summary", {})
        print(f"\n📊 주요 성능 지표:")
        print(f"  최대 처리량: {summary.get('max_throughput_docs_per_sec', 0):.1f} docs/sec")
        print(f"  메모리 효율성: {summary.get('memory_efficiency_kb_per_item', 0):.1f} KB/item")
        print(f"  동시성 효율성: {summary.get('max_concurrent_efficiency', 0):.1f}")
        print(f"  확장성 안정성: {summary.get('scalability_stability', 0):.1%}")
        print(f"  스트레스 복구: {'성공' if summary.get('stress_recovery_success', False) else '실패'}")
        
    except Exception as e:
        logger.error(f"성능 테스트 실행 중 오류 발생: {e}")
        print(f"\n❌ 성능 테스트 실패: {e}")
    
    print("\n=== 성능 검증 테스트 완료 ===")


if __name__ == "__main__":
    asyncio.run(main())