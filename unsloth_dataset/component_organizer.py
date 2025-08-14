#!/usr/bin/env python3
"""
컴포넌트별 데이터셋 조직화 모듈
Syncfusion 컴포넌트별로 데이터셋을 그룹화하고 계층 구조를 유지하는 기능을 제공합니다.
"""

import json
import logging
from typing import List, Dict, Any, Optional, Set, Tuple
from dataclasses import dataclass, field
from pathlib import Path
from collections import defaultdict
import re

logger = logging.getLogger(__name__)


@dataclass
class ComponentHierarchy:
    """컴포넌트 계층 구조 정보"""
    name: str
    category: str
    parent: Optional[str] = None
    children: List[str] = field(default_factory=list)
    description: str = ""
    priority: int = 0  # 훈련 우선순위 (높을수록 우선)


@dataclass
class ComponentDataset:
    """컴포넌트별 데이터셋"""
    component_name: str
    category: str
    samples: List[Dict[str, Any]] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    statistics: Dict[str, Any] = field(default_factory=dict)


@dataclass
class OrganizationConfig:
    """조직화 설정"""
    min_samples_per_component: int = 10
    max_samples_per_component: int = 1000
    enable_hierarchical_grouping: bool = True
    enable_category_balancing: bool = True
    priority_based_sampling: bool = True
    output_separate_files: bool = True
    include_mixed_category: bool = True
    mixed_category_ratio: float = 0.1  # 전체의 10%를 혼합 카테고리로


class ComponentOrganizer:
    """컴포넌트별 데이터셋 조직화 클래스"""
    
    def __init__(self, config: OrganizationConfig):
        """
        컴포넌트 조직화기를 초기화합니다.
        
        Args:
            config: 조직화 설정
        """
        self.config = config
        self.logger = logging.getLogger(__name__)
        
        # Syncfusion 컴포넌트 계층 구조 정의
        self.component_hierarchy = self._initialize_component_hierarchy()
        
        # 카테고리별 컴포넌트 매핑
        self.category_mapping = self._build_category_mapping()
        
        self.logger.info(f"ComponentOrganizer initialized with {len(self.component_hierarchy)} components")
    
    def _initialize_component_hierarchy(self) -> Dict[str, ComponentHierarchy]:
        """Syncfusion 컴포넌트 계층 구조를 초기화합니다."""
        components = {
            # 데이터 처리 및 분석
            "calculate": ComponentHierarchy(
                name="calculate", 
                category="data_processing",
                description="계산 엔진 및 수식 처리",
                priority=8
            ),
            "grid": ComponentHierarchy(
                name="grid", 
                category="data_display",
                description="데이터 그리드 컨트롤",
                priority=9
            ),
            "grouping": ComponentHierarchy(
                name="grouping", 
                category="data_display",
                description="데이터 그룹화 기능",
                priority=7
            ),
            "PivotGrid": ComponentHierarchy(
                name="PivotGrid", 
                category="data_analysis",
                description="피벗 테이블 및 분석",
                priority=8
            ),
            
            # 차트 및 시각화
            "chart": ComponentHierarchy(
                name="chart", 
                category="visualization",
                description="차트 및 그래프 컨트롤",
                priority=9
            ),
            "diagram": ComponentHierarchy(
                name="diagram", 
                category="visualization",
                description="다이어그램 및 플로우차트",
                priority=7
            ),
            "Gauge": ComponentHierarchy(
                name="Gauge", 
                category="visualization",
                description="게이지 및 미터 컨트롤",
                priority=6
            ),
            
            # 문서 처리
            "DocIo": ComponentHierarchy(
                name="DocIo", 
                category="document_processing",
                description="Word 문서 처리",
                priority=8
            ),
            "pdf": ComponentHierarchy(
                name="pdf", 
                category="document_processing",
                description="PDF 처리 기능",
                priority=8
            ),
            "PDF-Viewer": ComponentHierarchy(
                name="PDF-Viewer", 
                category="document_processing",
                description="PDF 뷰어 컨트롤",
                priority=7
            ),
            "XlsIO": ComponentHierarchy(
                name="XlsIO", 
                category="document_processing",
                description="Excel 파일 처리",
                priority=9
            ),
            
            # 편집 및 입력
            "edit": ComponentHierarchy(
                name="edit", 
                category="input_controls",
                description="텍스트 편집 컨트롤",
                priority=8
            ),
            
            # 스케줄링 및 시간 관리
            "schedule": ComponentHierarchy(
                name="schedule", 
                category="scheduling",
                description="스케줄러 및 캘린더",
                priority=7
            ),
            
            # 의료 및 특수 용도
            "DICOM": ComponentHierarchy(
                name="DICOM", 
                category="medical",
                description="의료 영상 처리",
                priority=5
            ),
            
            # 웹 및 UI
            "HTMLUI": ComponentHierarchy(
                name="HTMLUI", 
                category="web_ui",
                description="HTML UI 컨트롤",
                priority=6
            ),
            
            # 분석 및 OLAP
            "Olap-Common": ComponentHierarchy(
                name="Olap-Common", 
                category="data_analysis",
                description="OLAP 공통 기능",
                priority=6
            ),
            
            # 프로젝트 관리
            "ProjIO": ComponentHierarchy(
                name="ProjIO", 
                category="project_management",
                description="프로젝트 파일 처리",
                priority=5
            ),
            
            # 테스트 및 품질
            "QTP": ComponentHierarchy(
                name="QTP", 
                category="testing",
                description="테스트 자동화",
                priority=4
            ),
            
            # 도구 및 유틸리티
            "tools": ComponentHierarchy(
                name="tools", 
                category="utilities",
                description="개발 도구 및 유틸리티",
                priority=6
            ),
            "common": ComponentHierarchy(
                name="common", 
                category="utilities",
                description="공통 기능 및 유틸리티",
                priority=7
            )
        }
        
        return components
    
    def _build_category_mapping(self) -> Dict[str, List[str]]:
        """카테고리별 컴포넌트 매핑을 구축합니다."""
        mapping = defaultdict(list)
        
        for component_name, hierarchy in self.component_hierarchy.items():
            mapping[hierarchy.category].append(component_name)
        
        return dict(mapping)
    
    def organize_by_components(
        self, 
        samples: List[Dict[str, Any]]
    ) -> Dict[str, ComponentDataset]:
        """
        샘플을 컴포넌트별로 조직화합니다.
        
        Args:
            samples: 조직화할 샘플 목록
            
        Returns:
            컴포넌트별 데이터셋 딕셔너리
        """
        self.logger.info(f"Organizing {len(samples)} samples by components")
        
        # 컴포넌트별 샘플 분류
        component_samples = defaultdict(list)
        unclassified_samples = []
        
        for sample in samples:
            component = self._identify_component(sample)
            if component:
                component_samples[component].append(sample)
            else:
                unclassified_samples.append(sample)
        
        self.logger.info(f"Classified samples: {len(component_samples)} components, "
                        f"{len(unclassified_samples)} unclassified")
        
        # 컴포넌트별 데이터셋 생성
        organized_datasets = {}
        
        for component_name, comp_samples in component_samples.items():
            if len(comp_samples) >= self.config.min_samples_per_component:
                # 샘플 수 제한
                if len(comp_samples) > self.config.max_samples_per_component:
                    # 우선순위 기반 샘플링
                    if self.config.priority_based_sampling:
                        comp_samples = self._priority_sample(
                            comp_samples, 
                            self.config.max_samples_per_component
                        )
                    else:
                        comp_samples = comp_samples[:self.config.max_samples_per_component]
                
                # 컴포넌트 데이터셋 생성
                hierarchy = self.component_hierarchy.get(component_name)
                dataset = ComponentDataset(
                    component_name=component_name,
                    category=hierarchy.category if hierarchy else "unknown",
                    samples=comp_samples,
                    metadata={
                        "component_info": hierarchy.__dict__ if hierarchy else {},
                        "sample_count": len(comp_samples),
                        "avg_quality_score": self._calculate_avg_quality(comp_samples)
                    }
                )
                
                organized_datasets[component_name] = dataset
                self.logger.info(f"Component '{component_name}': {len(comp_samples)} samples")
        
        # 미분류 샘플 처리
        if unclassified_samples and self.config.include_mixed_category:
            mixed_dataset = ComponentDataset(
                component_name="mixed",
                category="mixed",
                samples=unclassified_samples,
                metadata={
                    "component_info": {"description": "Mixed component samples"},
                    "sample_count": len(unclassified_samples),
                    "avg_quality_score": self._calculate_avg_quality(unclassified_samples)
                }
            )
            organized_datasets["mixed"] = mixed_dataset
            self.logger.info(f"Mixed category: {len(unclassified_samples)} samples")
        
        return organized_datasets
    
    def organize_by_categories(
        self, 
        component_datasets: Dict[str, ComponentDataset]
    ) -> Dict[str, List[ComponentDataset]]:
        """
        컴포넌트 데이터셋을 카테고리별로 조직화합니다.
        
        Args:
            component_datasets: 컴포넌트별 데이터셋
            
        Returns:
            카테고리별 데이터셋 목록
        """
        self.logger.info("Organizing datasets by categories")
        
        category_datasets = defaultdict(list)
        
        for dataset in component_datasets.values():
            category_datasets[dataset.category].append(dataset)
        
        # 카테고리별 통계 계산
        for category, datasets in category_datasets.items():
            total_samples = sum(len(ds.samples) for ds in datasets)
            avg_quality = sum(ds.metadata.get("avg_quality_score", 0) for ds in datasets) / len(datasets)
            
            self.logger.info(f"Category '{category}': {len(datasets)} components, "
                           f"{total_samples} total samples, avg quality: {avg_quality:.3f}")
        
        return dict(category_datasets)
    
    def create_balanced_splits(
        self, 
        component_datasets: Dict[str, ComponentDataset],
        train_ratio: float = 0.8
    ) -> Tuple[Dict[str, ComponentDataset], Dict[str, ComponentDataset]]:
        """
        균형잡힌 훈련/검증 분할을 생성합니다.
        
        Args:
            component_datasets: 컴포넌트별 데이터셋
            train_ratio: 훈련 데이터 비율
            
        Returns:
            (훈련 데이터셋, 검증 데이터셋) 튜플
        """
        self.logger.info("Creating balanced train/validation splits")
        
        train_datasets = {}
        val_datasets = {}
        
        for component_name, dataset in component_datasets.items():
            samples = dataset.samples.copy()
            
            # 품질 점수 기반 정렬 (높은 품질부터)
            samples.sort(key=lambda x: x.get("quality_score", 0), reverse=True)
            
            # 분할 지점 계산
            split_point = int(len(samples) * train_ratio)
            
            # 훈련 데이터셋
            train_dataset = ComponentDataset(
                component_name=component_name,
                category=dataset.category,
                samples=samples[:split_point],
                metadata={
                    **dataset.metadata,
                    "split": "train",
                    "sample_count": split_point
                }
            )
            train_datasets[component_name] = train_dataset
            
            # 검증 데이터셋
            val_dataset = ComponentDataset(
                component_name=component_name,
                category=dataset.category,
                samples=samples[split_point:],
                metadata={
                    **dataset.metadata,
                    "split": "validation",
                    "sample_count": len(samples) - split_point
                }
            )
            val_datasets[component_name] = val_dataset
            
            self.logger.debug(f"Component '{component_name}': {split_point} train, "
                            f"{len(samples) - split_point} validation")
        
        return train_datasets, val_datasets
    
    def create_category_specific_datasets(
        self, 
        category_datasets: Dict[str, List[ComponentDataset]],
        target_samples_per_category: int = 500
    ) -> Dict[str, List[Dict[str, Any]]]:
        """
        카테고리별 특화 데이터셋을 생성합니다.
        
        Args:
            category_datasets: 카테고리별 데이터셋 목록
            target_samples_per_category: 카테고리당 목표 샘플 수
            
        Returns:
            카테고리별 통합 샘플 목록
        """
        self.logger.info("Creating category-specific datasets")
        
        category_samples = {}
        
        for category, datasets in category_datasets.items():
            # 카테고리 내 모든 샘플 수집
            all_samples = []
            for dataset in datasets:
                for sample in dataset.samples:
                    # 컴포넌트 정보 추가
                    enhanced_sample = sample.copy()
                    enhanced_sample["component"] = dataset.component_name
                    enhanced_sample["category"] = category
                    all_samples.append(enhanced_sample)
            
            # 품질 점수 기반 정렬 및 샘플링
            all_samples.sort(key=lambda x: x.get("quality_score", 0), reverse=True)
            
            if len(all_samples) > target_samples_per_category:
                selected_samples = all_samples[:target_samples_per_category]
            else:
                selected_samples = all_samples
            
            category_samples[category] = selected_samples
            
            self.logger.info(f"Category '{category}': {len(selected_samples)} samples "
                           f"from {len(datasets)} components")
        
        return category_samples
    
    def _identify_component(self, sample: Dict[str, Any]) -> Optional[str]:
        """샘플에서 컴포넌트를 식별합니다."""
        # 소스 정보에서 컴포넌트 추출
        source = sample.get("source", "")
        if isinstance(source, str):
            # 파일 경로에서 컴포넌트 추출
            for component_name in self.component_hierarchy.keys():
                if component_name.lower() in source.lower():
                    return component_name
        
        # 메타데이터에서 컴포넌트 추출
        metadata = sample.get("metadata", {})
        if isinstance(metadata, dict):
            component = metadata.get("component")
            if component and component in self.component_hierarchy:
                return component
        
        # 콘텐츠에서 컴포넌트 키워드 검색
        content_fields = ["instruction", "response", "content", "text"]
        for field in content_fields:
            content = sample.get(field, "")
            if isinstance(content, str):
                for component_name in self.component_hierarchy.keys():
                    # 대소문자 구분 없이 검색
                    if re.search(rf'\b{re.escape(component_name)}\b', content, re.IGNORECASE):
                        return component_name
        
        return None
    
    def _priority_sample(
        self, 
        samples: List[Dict[str, Any]], 
        target_count: int
    ) -> List[Dict[str, Any]]:
        """우선순위 기반 샘플링을 수행합니다."""
        # 품질 점수와 다양성을 고려한 샘플링
        samples_with_score = []
        
        for sample in samples:
            quality_score = sample.get("quality_score", 0.5)
            diversity_score = self._calculate_diversity_score(sample, samples)
            combined_score = quality_score * 0.7 + diversity_score * 0.3
            
            samples_with_score.append((combined_score, sample))
        
        # 점수 기준 정렬 및 상위 샘플 선택
        samples_with_score.sort(key=lambda x: x[0], reverse=True)
        return [sample for _, sample in samples_with_score[:target_count]]
    
    def _calculate_diversity_score(
        self, 
        sample: Dict[str, Any], 
        all_samples: List[Dict[str, Any]]
    ) -> float:
        """샘플의 다양성 점수를 계산합니다."""
        # 간단한 다양성 점수 계산 (실제로는 더 복잡한 알고리즘 사용 가능)
        instruction = sample.get("instruction", "")
        if not instruction:
            return 0.5
        
        # 길이 기반 다양성
        length_score = min(len(instruction) / 200, 1.0)
        
        # 키워드 다양성 (간단한 구현)
        words = set(instruction.lower().split())
        unique_words = len(words)
        diversity_score = min(unique_words / 20, 1.0)
        
        return (length_score + diversity_score) / 2
    
    def _calculate_avg_quality(self, samples: List[Dict[str, Any]]) -> float:
        """샘플들의 평균 품질 점수를 계산합니다."""
        if not samples:
            return 0.0
        
        total_quality = sum(sample.get("quality_score", 0.5) for sample in samples)
        return total_quality / len(samples)
    
    def generate_organization_report(
        self, 
        component_datasets: Dict[str, ComponentDataset],
        category_datasets: Dict[str, List[ComponentDataset]]
    ) -> Dict[str, Any]:
        """조직화 리포트를 생성합니다."""
        report = {
            "summary": {
                "total_components": len(component_datasets),
                "total_categories": len(category_datasets),
                "total_samples": sum(len(ds.samples) for ds in component_datasets.values())
            },
            "components": {},
            "categories": {},
            "recommendations": []
        }
        
        # 컴포넌트별 정보
        for name, dataset in component_datasets.items():
            report["components"][name] = {
                "category": dataset.category,
                "sample_count": len(dataset.samples),
                "avg_quality_score": dataset.metadata.get("avg_quality_score", 0),
                "priority": self.component_hierarchy.get(name, ComponentHierarchy("", "")).priority
            }
        
        # 카테고리별 정보
        for category, datasets in category_datasets.items():
            total_samples = sum(len(ds.samples) for ds in datasets)
            avg_quality = sum(ds.metadata.get("avg_quality_score", 0) for ds in datasets) / len(datasets)
            
            report["categories"][category] = {
                "component_count": len(datasets),
                "total_samples": total_samples,
                "avg_quality_score": avg_quality,
                "components": [ds.component_name for ds in datasets]
            }
        
        # 권장사항 생성
        report["recommendations"] = self._generate_recommendations(component_datasets, category_datasets)
        
        return report
    
    def _generate_recommendations(
        self, 
        component_datasets: Dict[str, ComponentDataset],
        category_datasets: Dict[str, List[ComponentDataset]]
    ) -> List[str]:
        """조직화 기반 권장사항을 생성합니다."""
        recommendations = []
        
        # 샘플 수가 적은 컴포넌트 식별
        low_sample_components = [
            name for name, dataset in component_datasets.items()
            if len(dataset.samples) < self.config.min_samples_per_component * 2
        ]
        
        if low_sample_components:
            recommendations.append(
                f"다음 컴포넌트들의 샘플 수가 부족합니다: {', '.join(low_sample_components[:5])}"
            )
        
        # 품질이 낮은 카테고리 식별
        low_quality_categories = []
        for category, datasets in category_datasets.items():
            avg_quality = sum(ds.metadata.get("avg_quality_score", 0) for ds in datasets) / len(datasets)
            if avg_quality < 0.6:
                low_quality_categories.append(category)
        
        if low_quality_categories:
            recommendations.append(
                f"다음 카테고리들의 품질 개선이 필요합니다: {', '.join(low_quality_categories)}"
            )
        
        # 균형 잡힌 훈련을 위한 권장사항
        category_sizes = {
            category: sum(len(ds.samples) for ds in datasets)
            for category, datasets in category_datasets.items()
        }
        
        max_size = max(category_sizes.values())
        min_size = min(category_sizes.values())
        
        if max_size > min_size * 3:
            recommendations.append(
                "카테고리 간 샘플 수 불균형이 심합니다. 균형 잡힌 샘플링을 고려하세요."
            )
        
        return recommendations