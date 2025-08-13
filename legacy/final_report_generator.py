#!/usr/bin/env python3
"""
Syncfusion WinForms Tool Calling Dataset Final Report Generator
최종 결과 보고서를 생성합니다.
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class FinalReportGenerator:
    """최종 보고서 생성기"""
    
    def __init__(self):
        self.report_data = {}
        
    def load_data(self):
        """데이터 로드"""
        # 데이터셋 로드
        try:
            with open('syncfusion_winforms_comprehensive_dataset.json', 'r', encoding='utf-8') as f:
                self.dataset = json.load(f)
            logger.info("Dataset loaded successfully")
        except FileNotFoundError:
            logger.error("Dataset file not found")
            raise
        
        # 검증 보고서 로드
        try:
            with open('dataset_validation_report.json', 'r', encoding='utf-8') as f:
                self.validation_report = json.load(f)
            logger.info("Validation report loaded successfully")
        except FileNotFoundError:
            logger.error("Validation report file not found")
            raise
        
        # API 시그니처 파일 로드
        try:
            with open('api_signatures.json', 'r', encoding='utf-8') as f:
                self.api_signatures = json.load(f)
            logger.info("API signatures loaded successfully")
        except FileNotFoundError:
            logger.error("API signatures file not found")
            raise
    
    def generate_executive_summary(self) -> Dict[str, Any]:
        """실행 요약 생성"""
        logger.info("Generating executive summary...")
        
        metadata = self.dataset.get('metadata', {})
        components = self.dataset.get('components', {})
        templates = self.dataset.get('templates', {})
        api_metadata = self.api_signatures.get('metadata', {})
        
        return {
            'project_overview': {
                'project_name': 'Syncfusion WinForms Tool Calling Dataset Generation',
                'objective': 'Generate comprehensive tool calling dataset for Syncfusion WinForms components',
                'start_date': '2025-08-12',
                'completion_date': datetime.now().strftime('%Y-%m-%d'),
                'total_duration': 'Completed in one session'
            },
            'key_metrics': {
                'total_components_processed': len(components),
                'total_templates_generated': metadata.get('total_templates', 0),
                'total_api_signatures_extracted': api_metadata.get('total_apis', 0),
                'total_documentation_pages': sum(comp.get('page_count', 0) for comp in components.values()),
                'dataset_file_size_mb': Path('syncfusion_winforms_comprehensive_dataset.json').stat().st_size / (1024 * 1024),
                'validation_score': self.validation_report['statistics']['quality_metrics']['completeness_score']
            },
            'major_achievements': [
                f"Successfully processed {len(components)} Syncfusion WinForms components",
                f"Generated {metadata.get('total_templates', 0)} tool calling templates",
                f"Extracted {api_metadata.get('total_apis', 0)} API signatures from documentation",
                f"Achieved {self.validation_report['statistics']['quality_metrics']['completeness_score']:.1f}% data completeness",
                "Created comprehensive validation framework",
                "Generated detailed quality metrics and statistics"
            ]
        }
    
    def generate_component_analysis(self) -> Dict[str, Any]:
        """컴포넌트 분석 생성"""
        logger.info("Generating component analysis...")
        
        components = self.dataset.get('components', {})
        api_components = self.api_signatures.get('components', {})
        
        # 컴포넌트별 상세 분석
        component_details = []
        total_apis = 0
        total_pages = 0
        
        for comp_name, comp_data in components.items():
            api_count = comp_data.get('api_count', 0)
            page_count = comp_data.get('page_count', 0)
            total_apis += api_count
            total_pages += page_count
            
            # 실제 API 시그니처 수와 비교
            actual_apis = len(api_components.get(comp_name, {}).get('api_signatures', []))
            api_coverage = (api_count / actual_apis * 100) if actual_apis > 0 else 0
            
            component_details.append({
                'name': comp_name,
                'category': comp_data.get('category', 'Unknown'),
                'description': comp_data.get('description', ''),
                'template_count': len([t for t in self.dataset.get('templates', []) if t.get('component') == comp_name]),
                'api_count': api_count,
                'actual_api_count': actual_apis,
                'api_coverage_percent': api_coverage,
                'page_count': page_count,
                'features': comp_data.get('features', []),
                'complexity_distribution': self.get_component_complexity_distribution(comp_name)
            })
        
        # 컴포넌트 카테고리별 분석
        category_analysis = {}
        for comp_name, comp_data in components.items():
            category = comp_data.get('category', 'Unknown')
            if category not in category_analysis:
                category_analysis[category] = {
                    'component_count': 0,
                    'total_apis': 0,
                    'total_pages': 0,
                    'total_templates': 0
                }
            
            category_analysis[category]['component_count'] += 1
            category_analysis[category]['total_apis'] += comp_data.get('api_count', 0)
            category_analysis[category]['total_pages'] += comp_data.get('page_count', 0)
            category_analysis[category]['total_templates'] += len([t for t in self.dataset.get('templates', []) if t.get('component') == comp_name])
        
        return {
            'summary': {
                'total_components': len(components),
                'total_apis_across_components': total_apis,
                'total_pages_across_components': total_pages,
                'average_apis_per_component': total_apis / len(components) if components else 0,
                'average_pages_per_component': total_pages / len(components) if components else 0,
                'largest_component_by_pages': max(components.items(), key=lambda x: x[1].get('page_count', 0))[0] if components else None,
                'most_api_rich_component': max(components.items(), key=lambda x: x[1].get('api_count', 0))[0] if components else None
            },
            'category_analysis': category_analysis,
            'component_details': component_details,
            'top_components_by_templates': sorted(
                [(comp_name, len([t for t in self.dataset.get('templates', []) if t.get('component') == comp_name])) 
                 for comp_name in components.keys()],
                key=lambda x: x[1], reverse=True
            )[:10]
        }
    
    def get_component_complexity_distribution(self, component_name: str) -> Dict[str, int]:
        """컴포넌트별 복잡도 분포 가져오기"""
        templates = [t for t in self.dataset.get('templates', []) if t.get('component') == component_name]
        distribution = {'low': 0, 'medium': 0, 'high': 0}
        
        for template in templates:
            complexity = template.get('complexity', 'unknown')
            if complexity in distribution:
                distribution[complexity] += 1
        
        return distribution
    
    def generate_template_analysis(self) -> Dict[str, Any]:
        """템플릿 분석 생성"""
        logger.info("Generating template analysis...")
        
        templates = self.dataset.get('templates', [])
        
        if not templates:
            return {'error': 'No templates found'}
        
        # 복잡도 분포
        complexity_dist = {}
        for template in templates:
            complexity = template.get('complexity', 'unknown')
            complexity_dist[complexity] = complexity_dist.get(complexity, 0) + 1
        
        # 카테고리 분포
        category_dist = {}
        for template in templates:
            category = template.get('category', 'unknown')
            category_dist[category] = category_dist.get(category, 0) + 1
        
        # 컴포넌트별 템플릿 수
        component_dist = {}
        for template in templates:
            component = template.get('component', 'unknown')
            component_dist[component] = component_dist.get(component, 0) + 1
        
        # 태그 분석
        all_tags = []
        for template in templates:
            all_tags.extend(template.get('tags', []))
        
        tag_dist = {}
        for tag in all_tags:
            tag_dist[tag] = tag_dist.get(tag, 0) + 1
        
        # 파라미터 분석
        parameter_analysis = self.analyze_parameters(templates)
        
        return {
            'summary': {
                'total_templates': len(templates),
                'average_tags_per_template': sum(len(t.get('tags', [])) for t in templates) / len(templates),
                'most_common_complexity': max(complexity_dist.items(), key=lambda x: x[1])[0] if complexity_dist else None,
                'most_common_category': max(category_dist.items(), key=lambda x: x[1])[0] if category_dist else None,
                'most_common_component': max(component_dist.items(), key=lambda x: x[1])[0] if component_dist else None
            },
            'complexity_distribution': complexity_dist,
            'category_distribution': category_dist,
            'component_distribution': component_dist,
            'tag_analysis': {
                'total_unique_tags': len(tag_dist),
                'most_common_tags': sorted(tag_dist.items(), key=lambda x: x[1], reverse=True)[:20],
                'tag_coverage': len([tag for tag in tag_dist if tag_dist[tag] > 1]) / len(tag_dist) * 100 if tag_dist else 0
            },
            'parameter_analysis': parameter_analysis
        }
    
    def analyze_parameters(self, templates: List[Dict]) -> Dict[str, Any]:
        """파라미터 분석"""
        total_templates = len(templates)
        templates_with_params = 0
        total_params = 0
        param_types = {}
        
        for template in templates:
            parameters = template.get('parameters', {})
            if parameters:
                templates_with_params += 1
                total_params += len(parameters)
                
                for param_name, param_info in parameters.items():
                    param_type = param_info.get('type', 'unknown')
                    param_types[param_type] = param_types.get(param_type, 0) + 1
        
        return {
            'templates_with_parameters': templates_with_params,
            'total_parameters': total_params,
            'average_parameters_per_template': total_params / total_templates if total_templates > 0 else 0,
            'parameter_coverage': templates_with_params / total_templates * 100 if total_templates > 0 else 0,
            'parameter_type_distribution': param_types
        }
    
    def generate_quality_analysis(self) -> Dict[str, Any]:
        """품질 분석 생성"""
        logger.info("Generating quality analysis...")
        
        validation_results = self.validation_report.get('validation_results', {})
        statistics = self.validation_report.get('statistics', {})
        
        # 전체 유효성 검사 결과
        overall_valid = all([
            validation_results.get('metadata', {}).get('valid', False),
            validation_results.get('components', {}).get('valid', False),
            validation_results.get('templates', {}).get('valid', False)
        ])
        
        # 오류 및 경고 통계
        total_errors = (
            len(validation_results.get('metadata', {}).get('errors', [])) +
            len(validation_results.get('components', {}).get('errors', [])) +
            len(validation_results.get('templates', {}).get('errors', []))
        )
        
        total_warnings = (
            len(validation_results.get('metadata', {}).get('warnings', [])) +
            len(validation_results.get('components', {}).get('warnings', [])) +
            len(validation_results.get('templates', {}).get('warnings', []))
        )
        
        # 완성도 점수
        completeness_score = statistics.get('quality_metrics', {}).get('completeness_score', 0)
        
        # 데이터 일관성 검사
        consistency_issues = self.check_data_consistency()
        
        return {
            'overall_quality': {
                'is_valid': overall_valid,
                'validation_score': completeness_score,
                'quality_rating': self.get_quality_rating(completeness_score),
                'recommendations': self.validation_report.get('recommendations', [])
            },
            'validation_summary': {
                'total_errors': total_errors,
                'total_warnings': total_warnings,
                'metadata_valid': validation_results.get('metadata', {}).get('valid', False),
                'components_valid': validation_results.get('components', {}).get('valid', False),
                'templates_valid': validation_results.get('templates', {}).get('valid', False)
            },
            'consistency_analysis': {
                'consistency_issues': consistency_issues,
                'data_integrity_score': 100 - (len(consistency_issues) * 5)  # 각 이슈당 5점 감점
            },
            'improvement_suggestions': self.generate_improvement_suggestions()
        }
    
    def get_quality_rating(self, score: float) -> str:
        """품질 등급 부여"""
        if score >= 95:
            return "Excellent"
        elif score >= 85:
            return "Good"
        elif score >= 75:
            return "Fair"
        elif score >= 60:
            return "Poor"
        else:
            return "Critical"
    
    def check_data_consistency(self) -> List[str]:
        """데이터 일관성 검사"""
        issues = []
        
        components = self.dataset.get('components', {})
        templates = self.dataset.get('templates', {})
        
        # 컴포넌트 일관성 검사
        template_components = set(t.get('component', '') for t in templates)
        defined_components = set(components.keys())
        
        missing_components = template_components - defined_components
        if missing_components:
            issues.append(f"Templates reference undefined components: {missing_components}")
        
        # 템플릿 수 검사
        for comp_name, comp_data in components.items():
            expected_templates = comp_data.get('api_count', 0) * 3  # 예상 템플릿 수
            actual_templates = len([t for t in templates if t.get('component') == comp_name])
            
            if actual_templates < expected_templates * 0.5:  # 예상의 50% 미만
                issues.append(f"Component {comp_name} has fewer templates than expected: {actual_templates} vs {expected_templates}")
        
        return issues
    
    def generate_improvement_suggestions(self) -> List[str]:
        """개선 제안 생성"""
        suggestions = []
        
        # 데이터 완성도 기반 제안
        completeness_score = self.validation_report['statistics']['quality_metrics']['completeness_score']
        if completeness_score < 95:
            suggestions.append(f"Improve data completeness to 95%+ (current: {completeness_score:.1f}%)")
        
        # 템플릿 분포 기반 제안
        template_dist = self.validation_report['statistics']['template_analysis'].get('component_distribution', {})
        if template_dist:
            min_count = min(template_dist.values())
            max_count = max(template_dist.values())
            if max_count > min_count * 3:
                suggestions.append("Balance template distribution across components")
        
        # API 커버리지 기반 제안
        components = self.dataset.get('components', {})
        api_components = self.api_signatures.get('components', {})
        
        low_coverage_components = []
        for comp_name, comp_data in components.items():
            actual_apis = len(api_components.get(comp_name, {}).get('api_signatures', []))
            used_apis = comp_data.get('api_count', 0)
            coverage = (used_apis / actual_apis * 100) if actual_apis > 0 else 0
            
            if coverage < 80:
                low_coverage_components.append((comp_name, coverage))
        
        if low_coverage_components:
            suggestions.append(f"Improve API coverage for components: {', '.join([f'{name} ({coverage:.1f}%)' for name, coverage in low_coverage_components[:3]])}")
        
        # 품질 기반 제안
        total_errors = len(self.validation_report['validation_results']['metadata']['errors']) + \
                      len(self.validation_report['validation_results']['components']['errors']) + \
                      len(self.validation_report['validation_results']['templates']['errors'])
        
        if total_errors > 0:
            suggestions.append(f"Fix all validation errors ({total_errors} total)")
        
        return suggestions
    
    def generate_final_report(self) -> Dict[str, Any]:
        """최종 보고서 생성"""
        logger.info("Generating final report...")
        
        self.load_data()
        
        report = {
            'report_metadata': {
                'generated_at': datetime.now().isoformat(),
                'report_version': '1.0.0',
                'data_files': {
                    'dataset': 'syncfusion_winforms_comprehensive_dataset.json',
                    'validation_report': 'dataset_validation_report.json',
                    'api_signatures': 'api_signatures.json'
                }
            },
            'executive_summary': self.generate_executive_summary(),
            'component_analysis': self.generate_component_analysis(),
            'template_analysis': self.generate_template_analysis(),
            'quality_analysis': self.generate_quality_analysis(),
            'appendix': {
                'file_sizes': {
                    'dataset_mb': Path('syncfusion_winforms_comprehensive_dataset.json').stat().st_size / (1024 * 1024),
                    'validation_report_mb': Path('dataset_validation_report.json').stat().st_size / (1024 * 1024),
                    'api_signatures_mb': Path('api_signatures.json').stat().st_size / (1024 * 1024)
                },
                'generation_timeline': {
                    'started_at': '2025-08-12',
                    'completed_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'total_duration': 'Completed in one session'
                }
            }
        }
        
        return report
    
    def save_report(self, output_file: str = "syncfusion_winforms_final_report.json"):
        """보고서 저장"""
        report = self.generate_final_report()
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Final report saved to {output_file}")
        return output_file

def main():
    """메인 함수"""
    generator = FinalReportGenerator()
    report_file = generator.save_report()
    logger.info(f"Final report generation completed: {report_file}")

if __name__ == "__main__":
    main()