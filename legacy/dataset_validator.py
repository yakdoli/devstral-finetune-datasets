#!/usr/bin/env python3
"""
Syncfusion WinForms Tool Calling Dataset Validator
생성된 데이터셋의 품질을 검증하고 통계를 생성합니다.
"""

import json
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DatasetValidator:
    """데이터셋 검증기"""
    
    def __init__(self, dataset_file: str = "syncfusion_winforms_comprehensive_dataset.json"):
        self.dataset_file = dataset_file
        self.dataset = {}
        self.validation_results = {}
        
    def load_dataset(self):
        """데이터셋 로드"""
        try:
            with open(self.dataset_file, 'r', encoding='utf-8') as f:
                self.dataset = json.load(f)
            logger.info(f"Dataset loaded from {self.dataset_file}")
        except FileNotFoundError:
            logger.error(f"Dataset file not found: {self.dataset_file}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing dataset file: {e}")
            raise
    
    def validate_metadata(self) -> Dict[str, Any]:
        """메타데이터 검증"""
        logger.info("Validating metadata...")
        
        metadata = self.dataset.get('metadata', {})
        results = {
            'valid': True,
            'errors': [],
            'warnings': [],
            'info': {}
        }
        
        # 필수 필드 확인
        required_fields = ['generated_at', 'total_templates', 'total_components', 'generator_version']
        for field in required_fields:
            if field not in metadata:
                results['errors'].append(f"Missing required metadata field: {field}")
                results['valid'] = False
        
        # 데이터 타입 검증
        if 'generated_at' in metadata and not isinstance(metadata['generated_at'], str):
            results['errors'].append("generated_at should be a string")
            results['valid'] = False
        
        if 'total_templates' in metadata and not isinstance(metadata['total_templates'], int):
            results['errors'].append("total_templates should be an integer")
            results['valid'] = False
        
        if 'total_components' in metadata and not isinstance(metadata['total_components'], int):
            results['errors'].append("total_components should be an integer")
            results['valid'] = False
        
        # 정보 수집
        results['info'] = {
            'generated_at': metadata.get('generated_at'),
            'total_templates': metadata.get('total_templates', 0),
            'total_components': metadata.get('total_components', 0),
            'generator_version': metadata.get('generator_version', 'unknown')
        }
        
        return results
    
    def validate_components(self) -> Dict[str, Any]:
        """컴포넌트 데이터 검증"""
        logger.info("Validating components...")
        
        components = self.dataset.get('components', {})
        results = {
            'valid': True,
            'errors': [],
            'warnings': [],
            'info': {
                'total_components': len(components),
                'component_names': list(components.keys()),
                'categories': {},
                'api_counts': {},
                'page_counts': {}
            }
        }
        
        expected_categories = {
            "Data Grid", "Data Visualization", "Calculation", "Common", "Diagram",
            "Medical Imaging", "Document Processing", "Text Editor", "Gauges",
            "Business Intelligence", "UI Framework", "PDF Processing", "PDF Viewer",
            "Project Management", "Testing", "Scheduling", "Development Tools", "Spreadsheet"
        }
        
        for component_name, component_data in components.items():
            # 필수 필드 확인
            required_fields = ['name', 'description', 'category', 'api_count', 'page_count', 'features']
            for field in required_fields:
                if field not in component_data:
                    results['errors'].append(f"Component {component_name} missing required field: {field}")
                    results['valid'] = False
            
            # 카테고리 검증
            category = component_data.get('category', '')
            if category not in expected_categories:
                results['warnings'].append(f"Component {component_name} has unknown category: {category}")
            
            # API 수 검증
            api_count = component_data.get('api_count', 0)
            if not isinstance(api_count, int) or api_count < 0:
                results['errors'].append(f"Component {component_name} has invalid api_count: {api_count}")
                results['valid'] = False
            
            # 페이지 수 검증
            page_count = component_data.get('page_count', 0)
            if not isinstance(page_count, int) or page_count < 0:
                results['errors'].append(f"Component {component_name} has invalid page_count: {page_count}")
                results['valid'] = False
            
            # 기능 목록 검증
            features = component_data.get('features', [])
            if not isinstance(features, list):
                results['errors'].append(f"Component {component_name} features should be a list")
                results['valid'] = False
            
            # 통계 수집
            results['info']['categories'][category] = results['info']['categories'].get(category, 0) + 1
            results['info']['api_counts'][component_name] = api_count
            results['info']['page_counts'][component_name] = page_count
        
        return results
    
    def validate_templates(self) -> Dict[str, Any]:
        """템플릿 데이터 검증"""
        logger.info("Validating templates...")
        
        templates = self.dataset.get('templates', [])
        results = {
            'valid': True,
            'errors': [],
            'warnings': [],
            'info': {
                'total_templates': len(templates),
                'complexity_distribution': {},
                'category_distribution': {},
                'component_distribution': {},
                'tag_distribution': {}
            }
        }
        
        expected_complexities = {'low', 'medium', 'high'}
        expected_components = set(self.dataset.get('components', {}).keys())
        
        for i, template in enumerate(templates):
            # 필수 필드 확인
            required_fields = ['name', 'description', 'parameters', 'component', 'category', 'code_example', 'api_signature', 'complexity', 'tags']
            for field in required_fields:
                if field not in template:
                    results['errors'].append(f"Template {i} missing required field: {field}")
                    results['valid'] = False
            
            # 복잡도 검증
            complexity = template.get('complexity', '')
            if complexity not in expected_complexities:
                results['warnings'].append(f"Template {i} has unknown complexity: {complexity}")
            
            # 컴포넌트 검증
            component = template.get('component', '')
            if component not in expected_components:
                results['warnings'].append(f"Template {i} has unknown component: {component}")
            
            # 태그 검증
            tags = template.get('tags', [])
            if not isinstance(tags, list):
                results['errors'].append(f"Template {i} tags should be a list")
                results['valid'] = False
            
            # 통계 수집
            complexity = template.get('complexity', 'unknown')
            results['info']['complexity_distribution'][complexity] = results['info']['complexity_distribution'].get(complexity, 0) + 1
            
            category = template.get('category', 'unknown')
            results['info']['category_distribution'][category] = results['info']['category_distribution'].get(category, 0) + 1
            
            component = template.get('component', 'unknown')
            results['info']['component_distribution'][component] = results['info']['component_distribution'].get(component, 0) + 1
            
            for tag in tags:
                results['info']['tag_distribution'][tag] = results['info']['tag_distribution'].get(tag, 0) + 1
        
        return results
    
    def generate_statistics(self) -> Dict[str, Any]:
        """통계 생성"""
        logger.info("Generating statistics...")
        
        stats = {
            'dataset_overview': {},
            'component_analysis': {},
            'template_analysis': {},
            'quality_metrics': {}
        }
        
        # 데이터셋 개요
        metadata = self.dataset.get('metadata', {})
        components = self.dataset.get('components', {})
        templates = self.dataset.get('templates', [])
        
        stats['dataset_overview'] = {
            'generation_timestamp': metadata.get('generated_at'),
            'total_templates': len(templates),
            'total_components': len(components),
            'generator_version': metadata.get('generator_version'),
            'file_size_mb': Path(self.dataset_file).stat().st_size / (1024 * 1024) if Path(self.dataset_file).exists() else 0
        }
        
        # 컴포넌트 분석
        total_apis = sum(comp.get('api_count', 0) for comp in components.values())
        total_pages = sum(comp.get('page_count', 0) for comp in components.values())
        
        stats['component_analysis'] = {
            'total_apis_across_components': total_apis,
            'total_pages_across_components': total_pages,
            'average_apis_per_component': total_apis / len(components) if components else 0,
            'average_pages_per_component': total_pages / len(components) if components else 0,
            'component_with_most_apis': max(components.items(), key=lambda x: x[1].get('api_count', 0))[0] if components else None,
            'component_with_most_pages': max(components.items(), key=lambda x: x[1].get('page_count', 0))[0] if components else None
        }
        
        # 템플릿 분석
        if templates:
            complexities = [t.get('complexity', 'unknown') for t in templates]
            categories = [t.get('category', 'unknown') for t in templates]
            components_list = [t.get('component', 'unknown') for t in templates]
            
            stats['template_analysis'] = {
                'complexity_distribution': dict(zip(*zip(*[(c, complexities.count(c)) for c in set(complexities)]))),
                'category_distribution': dict(zip(*zip(*[(c, categories.count(c)) for c in set(categories)]))),
                'component_distribution': dict(zip(*zip(*[(c, components_list.count(c)) for c in set(components_list)]))),
                'average_tags_per_template': sum(len(t.get('tags', [])) for t in templates) / len(templates),
                'most_common_tags': sorted([(tag, sum(1 for t in templates if tag in t.get('tags', []))) for tag in set(tag for t in templates for tag in t.get('tags', []))], key=lambda x: x[1], reverse=True)[:10]
            }
        
        # 품질 지표
        validation_results = self.validate()
        stats['quality_metrics'] = {
            'overall_valid': validation_results['metadata']['valid'] and validation_results['components']['valid'] and validation_results['templates']['valid'],
            'total_errors': len(validation_results['metadata']['errors']) + len(validation_results['components']['errors']) + len(validation_results['templates']['errors']),
            'total_warnings': len(validation_results['metadata']['warnings']) + len(validation_results['components']['warnings']) + len(validation_results['templates']['warnings']),
            'completeness_score': self.calculate_completeness_score(validation_results)
        }
        
        return stats
    
    def calculate_completeness_score(self, validation_results: Dict[str, Any]) -> float:
        """완성도 점수 계산"""
        total_possible = 0
        total_achieved = 0
        
        # 메타데이터 완성도
        metadata_fields = ['generated_at', 'total_templates', 'total_components', 'generator_version']
        total_possible += len(metadata_fields)
        if validation_results['metadata']['valid']:
            total_achieved += len(metadata_fields)
        
        # 컴포넌트 완성도
        components = self.dataset.get('components', {})
        total_possible += len(components) * 6  # 6개 필드 per component
        for component_name, component_data in components.items():
            required_fields = ['name', 'description', 'category', 'api_count', 'page_count', 'features']
            for field in required_fields:
                if field in component_data:
                    total_achieved += 1
        
        # 템플릿 완성도
        templates = self.dataset.get('templates', [])
        total_possible += len(templates) * 9  # 9개 필드 per template
        for template in templates:
            required_fields = ['name', 'description', 'parameters', 'component', 'category', 'code_example', 'api_signature', 'complexity', 'tags']
            for field in required_fields:
                if field in template:
                    total_achieved += 1
        
        return (total_achieved / total_possible * 100) if total_possible > 0 else 0
    
    def validate(self) -> Dict[str, Any]:
        """전체 검증 수행"""
        self.load_dataset()
        
        results = {
            'metadata': self.validate_metadata(),
            'components': self.validate_components(),
            'templates': self.validate_templates(),
            'overall_valid': True
        }
        
        # 전체 유효성 검사
        results['overall_valid'] = all([
            results['metadata']['valid'],
            results['components']['valid'],
            results['templates']['valid']
        ])
        
        return results
    
    def save_validation_report(self, output_file: str = "dataset_validation_report.json"):
        """검증 보고서 저장"""
        validation_results = self.validate()
        statistics = self.generate_statistics()
        
        report = {
            'validation_timestamp': datetime.now().isoformat(),
            'validation_results': validation_results,
            'statistics': statistics,
            'recommendations': self.generate_recommendations(validation_results, statistics)
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Validation report saved to {output_file}")
        return output_file
    
    def generate_recommendations(self, validation_results: Dict[str, Any], statistics: Dict[str, Any]) -> List[str]:
        """개선 권장사항 생성"""
        recommendations = []
        
        # 오류 기반 권장사항
        all_errors = (validation_results['metadata']['errors'] + 
                     validation_results['components']['errors'] + 
                     validation_results['templates']['errors'])
        
        if all_errors:
            recommendations.append(f"Fix validation errors: {', '.join(all_errors[:3])}...")
        
        # 경고 기반 권장사항
        all_warnings = (validation_results['metadata']['warnings'] + 
                       validation_results['components']['warnings'] + 
                       validation_results['templates']['warnings'])
        
        if all_warnings:
            recommendations.append(f"Address validation warnings: {', '.join(all_warnings[:3])}...")
        
        # 통계 기반 권장사항
        completeness_score = statistics['quality_metrics']['completeness_score']
        if completeness_score < 95:
            recommendations.append(f"Improve data completeness (current: {completeness_score:.1f}%)")
        
        # 템플릿 분포 기반 권장사항
        template_dist = statistics['template_analysis'].get('component_distribution', {})
        if template_dist:
            min_templates = min(template_dist.values())
            max_templates = max(template_dist.values())
            if max_templates > min_templates * 3:
                recommendations.append("Consider balancing template distribution across components")
        
        return recommendations

def main():
    """메인 함수"""
    validator = DatasetValidator()
    report_file = validator.save_validation_report()
    logger.info(f"Dataset validation completed: {report_file}")

if __name__ == "__main__":
    main()