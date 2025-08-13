#!/usr/bin/env python3
"""
API Signature Extractor for Context7 MCP Integration
Extracts API information from Context7 data and matches with md_staging documentation
"""

import json
import re
import asyncio
from typing import List, Dict, Any, Optional, Set
from dataclasses import dataclass, asdict
from pathlib import Path
from datetime import datetime
import logging
from collections import defaultdict

# Context7 MCP 도구 임포트
try:
    from context7_connector import Context7Connector, get_context7_connector
    CONTEXT7_AVAILABLE = True
except ImportError:
    CONTEXT7_AVAILABLE = False
    logging.warning("Context7 MCP not available. Using fallback extraction methods.")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class APISignature:
    """API 시그니처 정보"""
    name: str
    namespace: str
    parameters: List[Dict[str, Any]]
    return_type: str
    description: str
    code_example: str
    component: str
    version: str = "latest"
    
@dataclass
class ComponentInfo:
    """컴포넌트 정보"""
    name: str
    category: str
    api_signatures: List[APISignature]
    documentation_paths: List[str]
    related_components: List[str]

class APISignatureExtractor:
    """API 시그니처 추출기 클래스"""
    
    def __init__(self, context7_library_id: str = "/yakdoli/syncfusion-v11-winform"):
        self.context7_library_id = context7_library_id
        self.context7_connector = get_context7_connector(use_mock=True) if CONTEXT7_AVAILABLE else None
        self.api_patterns = {
            'method': r'(?:public|private|protected|static|async)?\s*[\w<>]+\s+(\w+)\s*\([^)]*\)',
            'parameter': r'(\w+)\s*:\s*([\w<>[\],\s&|]+)',
            'return_type': r'->\s*([\w<>[\],\s&|]+)',
            'namespace': r'namespace\s+(\w+(?:\.\w+)*)',
            'class': r'class\s+(\w+)',
            'property': r'(?:public|private|protected)?\s*(?:static)?\s*[\w<>]+\s+(\w+)\s*(?:\{get;set;\}|=>|;)',
            'event': r'(?:public|private|protected)?\s*event\s+([\w<>]+)\s+(\w+)',
        }
        
    def extract_api_from_code(self, code: str, component: str) -> List[APISignature]:
        """코드에서 API 시그니처 추출"""
        signatures = []
        
        # 메서드 추출
        method_pattern = re.compile(self.api_patterns['method'], re.MULTILINE)
        methods = method_pattern.findall(code)
        
        for method in methods:
            if method.lower() in ['class', 'namespace', 'public', 'private', 'protected', 'static', 'async']:
                continue
                
            # 파라미터 추출
            method_match = re.search(f'{method}\\s*\\(([^)]*)\\)', code)
            if method_match:
                params_text = method_match.group(1)
                parameters = self._extract_parameters(params_text)
                
                # 리턴 타입 추출
                return_type = "void"
                return_pattern = re.compile(f'{method}\\\\s*\\\\([^)]*\\\\)\\\\s*->\\\\s*([^{{]+)', re.MULTILINE)
                return_match = return_pattern.search(code)
                if return_match:
                    return_type = return_match.group(1).strip()
                
                # 설명 추출 (메서드 주석)
                description = self._extract_description(code, method)
                
                # 코드 예제 추출
                code_example = self._extract_code_example(code, method)
                
                signature = APISignature(
                    name=method,
                    namespace=component,
                    parameters=parameters,
                    return_type=return_type,
                    description=description,
                    code_example=code_example,
                    component=component
                )
                signatures.append(signature)
        
        # 속성 추출
        property_pattern = re.compile(self.api_patterns['property'], re.MULTILINE)
        properties = property_pattern.findall(code)
        
        for prop_name in properties:
            if prop_name.lower() in ['class', 'namespace', 'public', 'private', 'protected', 'static', 'async']:
                continue
                
            description = self._extract_description(code, prop_name)
            code_example = self._extract_code_example(code, prop_name)
            
            signature = APISignature(
                name=prop_name,
                namespace=component,
                parameters=[],
                return_type="object",
                description=f"Property: {description}",
                code_example=code_example,
                component=component
            )
            signatures.append(signature)
        
        # 이벤트 추출
        event_pattern = re.compile(self.api_patterns['event'], re.MULTILINE)
        events = event_pattern.findall(code)
        
        for event_type, event_name in events:
            description = self._extract_description(code, event_name)
            code_example = self._extract_code_example(code, event_name)
            
            signature = APISignature(
                name=event_name,
                namespace=component,
                parameters=[],
                return_type="void",
                description=f"Event: {description}",
                code_example=code_example,
                component=component
            )
            signatures.append(signature)
        
        return signatures
    
    def _extract_parameters(self, params_text: str) -> List[Dict[str, Any]]:
        """파라미터 텍스트에서 파라미터 정보 추출"""
        if not params_text.strip():
            return []
        
        parameters = []
        param_pattern = re.compile(self.api_patterns['parameter'])
        
        for param_match in param_pattern.finditer(params_text):
            name = param_match.group(1)
            param_type = param_match.group(2).strip()
            
            # 기본값 추출
            default_value = None
            if '=' in param_type:
                param_type, default_value = param_type.split('=', 1)
                default_value = default_value.strip()
            
            parameters.append({
                'name': name,
                'type': param_type,
                'default': default_value,
                'required': default_value is None
            })
        
        return parameters
    
    def _extract_description(self, code: str, method_name: str) -> str:
        """메서드 설명 추출"""
        # 주석에서 설명 추출
        comment_pattern = re.compile(r'//.*?$|/\*.*?\*/', re.MULTILINE | re.DOTALL)
        comments = comment_pattern.findall(code)
        
        for comment in comments:
            comment = re.sub(r'^\s*//\s*', '', comment, flags=re.MULTILINE)
            comment = re.sub(r'^\s*/\*\s*', '', comment)
            comment = re.sub(r'\s*\*/\s*$', '', comment)
            
            if method_name.lower() in comment.lower():
                return comment.strip()
        
        return f"API method for {method_name}"
    
    def _extract_code_example(self, code: str, method_name: str) -> str:
        """메서드 코드 예제 추출"""
        # 메서드 주변의 코드 블록 추출
        lines = code.split('\n')
        method_start = -1
        method_end = -1
        indent_level = 0
        
        for i, line in enumerate(lines):
            if method_name in line and '(' in line and ')' in line:
                method_start = i
                indent_level = len(line) - len(line.lstrip())
                break
        
        if method_start == -1:
            return ""
        
        # 메서드 본문 추출
        brace_count = 0
        for i in range(method_start, len(lines)):
            line = lines[i]
            if '{' in line:
                brace_count += line.count('{')
            if '}' in line:
                brace_count -= line.count('}')
            
            if brace_count == 0 and i > method_start:
                method_end = i
                break
        
        if method_end == -1:
            method_end = min(method_start + 10, len(lines))
        
        example_lines = lines[method_start:method_end + 1]
        return '\n'.join(example_lines)
    
    async def extract_from_context7(self, component_name: str) -> List[APISignature]:
        """Context7에서 API 정보 추출"""
        if not CONTEXT7_AVAILABLE or not self.context7_connector:
            logger.warning("Context7 MCP not available")
            return []
        
        try:
            # Context7 커넥터에서 스니펫 가져오기
            snippets = await self.context7_connector.get_component_snippets(component_name, max_snippets=100)
            
            # API 정보 추출
            signatures = []
            for snippet in snippets:
                extracted = self.extract_api_from_code(
                    snippet.code,
                    component_name
                )
                signatures.extend(extracted)
            
            logger.info(f"Extracted {len(signatures)} API signatures from Context7 for {component_name}")
            return signatures
            
        except Exception as e:
            logger.error(f"Error extracting from Context7: {e}")
            return []
    
    def match_with_md_staging(self, md_staging_path: Path) -> Dict[str, ComponentInfo]:
        """md_staging 데이터와 API 정보 매칭"""
        component_map = defaultdict(list)
        
        # md_staging에서 컴포넌트별 파일 분류
        for component_dir in md_staging_path.iterdir():
            if not component_dir.is_dir():
                continue
            
            component_name = component_dir.name
            md_files = list(component_dir.glob("page_*.md"))
            
            for md_file in md_files:
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # 코드 블록에서 API 추출
                    code_blocks = re.findall(r'```(?:csharp|cs|vb|vb.net)\n(.*?)```', content, re.DOTALL)
                    for code in code_blocks:
                        signatures = self.extract_api_from_code(code, component_name)
                        component_map[component_name].extend(signatures)
                
                except Exception as e:
                    logger.error(f"Error processing {md_file}: {e}")
                    continue
        
        # ComponentInfo 객체로 변환
        components = {}
        for component_name, signatures in component_map.items():
            components[component_name] = ComponentInfo(
                name=component_name,
                category=self._categorize_component(component_name),
                api_signatures=signatures,
                documentation_paths=[f"md_staging/{component_name}"],
                related_components=self._find_related_components(component_name)
            )
        
        logger.info(f"Matched {len(components)} components with API signatures")
        return components
    
    def _categorize_component(self, component_name: str) -> str:
        """컴포넌트 카테고리 분류"""
        category_mapping = {
            'calculate': 'Calculation',
            'chart': 'Charting',
            'grid': 'DataGrid',
            'diagram': 'Diagram',
            'pdf': 'PDF',
            'xlsio': 'Excel',
            'docio': 'Word',
            'htmlui': 'UI',
            'pivotgrid': 'Pivot',
            'schedule': 'Scheduling',
            'gauge': 'Gauge',
            'edit': 'Editor',
            'common': 'Common',
            'tools': 'Utilities'
        }
        
        for key, category in category_mapping.items():
            if key.lower() in component_name.lower():
                return category
        
        return 'General'
    
    def _find_related_components(self, component_name: str) -> List[str]:
        """관련 컴포넌트 찾기"""
        # 간단한 관계 매핑 (실제로는 더 복잡한 로직이 필요)
        relations = {
            'grid': ['common', 'calculate'],
            'chart': ['common', 'calculate'],
            'pdf': ['common'],
            'xlsio': ['common'],
            'docio': ['common'],
        }
        
        for key, related in relations.items():
            if key.lower() in component_name.lower():
                return related
        
        return []
    
    async def extract_all_apis(self, md_staging_path: Path, use_context7: bool = True) -> Dict[str, ComponentInfo]:
        """모든 컴포넌트에서 API 정보 추출"""
        # md_staging에서 기본 추출
        components = self.match_with_md_staging(md_staging_path)
        
        # Context7에서 추가 정보 추출
        if use_context7 and CONTEXT7_AVAILABLE:
            # Context7 연결
            await self.context7_connector.connect()
            
            try:
                for component_name in components.keys():
                    logger.info(f"Processing component: {component_name}")
                    context7_signatures = await self.extract_from_context7(component_name)
                    if context7_signatures:
                        # 기존 시그니처와 병합 (중복 제거 및 개선)
                        existing_names = {sig.name for sig in components[component_name].api_signatures}
                        enhanced_signatures = []
                        
                        for sig in context7_signatures:
                            if sig.name not in existing_names:
                                enhanced_signatures.append(sig)
                            else:
                                # 기존 시그니처 개선
                                for existing_sig in components[component_name].api_signatures:
                                    if existing_sig.name == sig.name:
                                        # 더 나은 설명이나 코드 예시로 업데이트
                                        if len(sig.description) > len(existing_sig.description):
                                            existing_sig.description = sig.description
                                        if len(sig.code_example) > len(existing_sig.code_example):
                                            existing_sig.code_example = sig.code_example
                                        break
                        
                        components[component_name].api_signatures.extend(enhanced_signatures)
                        logger.info(f"Enhanced {component_name} with {len(enhanced_signatures)} new APIs")
            
            finally:
                await self.context7_connector.disconnect()
        
        return components
    
    def save_api_signatures(self, components: Dict[str, ComponentInfo], output_path: Path):
        """API 시그니처 저장"""
        output_data = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'total_components': len(components),
                'total_apis': sum(len(comp.api_signatures) for comp in components.values())
            },
            'components': {name: asdict(comp) for name, comp in components.items()}
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"API signatures saved to {output_path}")

async def main():
    """메인 실행 함수"""
    extractor = APISignatureExtractor()
    md_staging_path = Path("md_staging")
    output_path = Path("api_signatures.json")
    
    if not md_staging_path.exists():
        logger.error(f"md_staging path does not exist: {md_staging_path}")
        return
    
    # API 정보 추출
    logger.info("Starting API signature extraction...")
    components = await extractor.extract_all_apis(md_staging_path, use_context7=True)
    
    # 결과 저장
    extractor.save_api_signatures(components, output_path)
    
    # 통계 출력
    total_apis = sum(len(comp.api_signatures) for comp in components.values())
    logger.info(f"Total APIs extracted: {total_apis}")
    logger.info(f"Components processed: {len(components)}")
    
    # 컴포넌트별 통계
    for component_name, component_info in components.items():
        logger.info(f"  {component_name}: {len(component_info.api_signatures)} APIs")

if __name__ == "__main__":
    asyncio.run(main())