#!/usr/bin/env python3
"""
Tool Calling Templates for Bilingual Dataset Generation
Implements Alpaca format-based tool calling definitions with API signature integration
"""

import json
import re
from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass, asdict
from datetime import datetime
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class ToolParameter:
    """Tool 파라미터 정의"""
    name: str
    type: str
    description: str
    required: bool = True
    default: Any = None
    enum: Optional[List[str]] = None
    
@dataclass
class ToolDefinition:
    """Tool calling 정의"""
    name: str
    description: str
    parameters: List[ToolParameter]
    component: str
    category: str
    api_signature: Optional[str] = None
    code_example: Optional[str] = None
    
@dataclass
class ToolCallTemplate:
    """Tool calling 템플릿"""
    instruction: str
    input: str
    output: str
    tool_name: str
    component: str
    category: str
    difficulty: str = "intermediate"
    tags: List[str] = None
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = []

class ToolCallingTemplateManager:
    """Tool calling 템플릿 관리자"""
    
    def __init__(self):
        self.definitions: Dict[str, ToolDefinition] = {}
        self.templates: Dict[str, List[ToolCallTemplate]] = {}
        self.type_mapping = {
            'string': 'string',
            'int': 'integer',
            'double': 'number',
            'bool': 'boolean',
            'object': 'object',
            'array': 'array'
        }
        
    def create_tool_definition(self, api_signature: Dict[str, Any]) -> ToolDefinition:
        """API 시그니처에서 Tool 정의 생성"""
        # 파라미터 변환
        parameters = []
        for param in api_signature.get('parameters', []):
            tool_param = ToolParameter(
                name=param['name'],
                type=self._map_parameter_type(param['type']),
                description=param.get('description', f"Parameter {param['name']}"),
                required=param.get('required', True),
                default=param.get('default'),
                enum=param.get('enum')
            )
            parameters.append(tool_param)
        
        # Tool 정의 생성
        tool_def = ToolDefinition(
            name=api_signature['name'],
            description=api_signature.get('description', f"API method for {api_signature['name']}"),
            parameters=parameters,
            component=api_signature['component'],
            category=self._categorize_tool(api_signature),
            api_signature=f"{api_signature.get('namespace', '')}.{api_signature['name']}",
            code_example=api_signature.get('code_example', '')
        )
        
        return tool_def
    
    def _map_parameter_type(self, param_type: str) -> str:
        """파라미터 타입 매핑"""
        param_type = param_type.lower().strip()
        
        # 기본 타입 매핑
        for source, target in self.type_mapping.items():
            if source in param_type:
                return target
        
        # 복잡한 타입 처리
        if 'list' in param_type or 'array' in param_type:
            return 'array'
        if 'dict' in param_type or 'object' in param_type:
            return 'object'
        
        return 'string'
    
    def _categorize_tool(self, api_signature: Dict[str, Any]) -> str:
        """Tool 카테고리 분류"""
        component = api_signature.get('component', '').lower()
        
        category_mapping = {
            'calculate': 'calculation',
            'chart': 'visualization',
            'grid': 'data',
            'diagram': 'diagram',
            'pdf': 'document',
            'xlsio': 'spreadsheet',
            'docio': 'document',
            'htmlui': 'ui',
            'pivotgrid': 'analysis',
            'schedule': 'planning',
            'gauge': 'indicator',
            'edit': 'editor',
            'common': 'utility',
            'tools': 'utility'
        }
        
        for key, category in category_mapping.items():
            if key in component:
                return category
        
        return 'general'
    
    def generate_tool_calling_template(self, tool_def: ToolDefinition, 
                                     difficulty: str = "intermediate") -> ToolCallTemplate:
        """Tool calling 템플릿 생성"""
        # 난이도별 프롬프트 템플릿
        prompt_templates = {
            'beginner': f"간단한 {tool_def.component} 컴포넌트 사용법을 알려주세요.",
            'intermediate': f"{tool_def.component} 컴포넌트에서 {tool_def.name} 메서드를 사용하는 방법을 설명해주세요.",
            'advanced': f"{tool_def.component} 컴포넌트의 고급 기능인 {tool_def.name} 메서드를 활용한 복잡한 시나리오를 구현해주세요."
        }
        
        # 입력 생성
        input_text = prompt_templates.get(difficulty, prompt_templates['intermediate'])
        
        # 출력 템플릿 생성
        output_template = self._create_output_template(tool_def)
        
        # 태그 생성
        tags = [tool_def.component, tool_def.category, tool_def.name]
        if difficulty != 'intermediate':
            tags.append(difficulty)
        
        template = ToolCallTemplate(
            instruction=input_text,
            input="",
            output=output_template,
            tool_name=tool_def.name,
            component=tool_def.component,
            category=tool_def.category,
            difficulty=difficulty,
            tags=tags
        )
        
        return template
    
    def _create_output_template(self, tool_def: ToolDefinition) -> str:
        """출력 템플릿 생성"""
        # 파라미터 설명 생성
        param_descriptions = []
        for param in tool_def.parameters:
            required_text = "(필수)" if param.required else "(선택)"
            default_text = f" (기본값: {param.default})" if param.default else ""
            param_descriptions.append(f"- {param.name}: {param.description} {required_text}{default_text}")
        
        # Tool calling 형식 생성
        tool_call_format = {
            "tool_name": tool_def.name,
            "parameters": {
                param.name: {
                    "type": param.type,
                    "description": param.description,
                    "required": param.required
                }
                for param in tool_def.parameters
            }
        }
        
        output_template = f"""## {tool_def.name} 사용법

### 설명
{tool_def.description}

### 파라미터
{chr(10).join(param_descriptions)}

### Tool Calling 예시
```json
{json.dumps(tool_call_format, indent=2, ensure_ascii=False)}
```

### 코드 예시
```csharp
{tool_def.code_example or '// 코드 예시가 없습니다'}
```

### 주의사항
- 필수 파라미터는 반드시 제공해야 합니다.
- 파라미터 타입에 맞는 값을 입력해주세요.
- 반환값은 해당 메서드의 실행 결과입니다."""
        
        return output_template
    
    def load_api_signatures(self, api_signatures_path: Path):
        """API 시그니처 파일 로드"""
        if not api_signatures_path.exists():
            logger.warning(f"API signatures file not found: {api_signatures_path}")
            return
        
        with open(api_signatures_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Tool 정의 생성
        for component_name, component_data in data.get('components', {}).items():
            for api_sig in component_data.get('api_signatures', []):
                tool_def = self.create_tool_definition(api_sig)
                self.definitions[tool_def.name] = tool_def
        
        logger.info(f"Loaded {len(self.definitions)} tool definitions")
    
    def generate_all_templates(self, difficulties: List[str] = None) -> Dict[str, List[ToolCallTemplate]]:
        """모든 Tool calling 템플릿 생성"""
        if difficulties is None:
            difficulties = ['beginner', 'intermediate', 'advanced']
        
        all_templates = {}
        
        for tool_name, tool_def in self.definitions.items():
            component_templates = []
            
            for difficulty in difficulties:
                template = self.generate_tool_calling_template(tool_def, difficulty)
                component_templates.append(template)
            
            all_templates[tool_name] = component_templates
        
        self.templates = all_templates
        logger.info(f"Generated {len(all_templates)} tool calling templates")
        
        return all_templates
    
    def filter_templates_by_category(self, category: str) -> List[ToolCallTemplate]:
        """카테고리별 템플릿 필터링"""
        filtered = []
        for tool_name, templates in self.templates.items():
            for template in templates:
                if template.category == category:
                    filtered.append(template)
        
        return filtered
    
    def filter_templates_by_component(self, component: str) -> List[ToolCallTemplate]:
        """컴포넌트별 템플릿 필터링"""
        filtered = []
        for tool_name, templates in self.templates.items():
            for template in templates:
                if template.component == component:
                    filtered.append(template)
        
        return filtered
    
    def export_templates(self, output_path: Path, format: str = 'json'):
        """템플릿 내보내기"""
        if not self.templates:
            logger.warning("No templates to export")
            return
        
        export_data = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'total_tools': len(self.templates),
                'total_templates': sum(len(templates) for templates in self.templates.values())
            },
            'templates': {}
        }
        
        # 템플릿 데이터 변환
        for tool_name, templates in self.templates.items():
            export_data['templates'][tool_name] = [asdict(template) for template in templates]
        
        # 파일 저장
        if format.lower() == 'json':
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)
        elif format.lower() == 'jsonl':
            with open(output_path, 'w', encoding='utf-8') as f:
                for tool_name, templates in self.templates.items():
                    for template in templates:
                        f.write(json.dumps(asdict(template), ensure_ascii=False) + '\n')
        else:
            raise ValueError(f"Unsupported format: {format}")
        
        logger.info(f"Templates exported to {output_path} ({format} format)")
    
    def get_template_statistics(self) -> Dict[str, Any]:
        """템플릿 통계 정보"""
        stats = {
            'total_tools': len(self.definitions),
            'total_templates': sum(len(templates) for templates in self.templates.values()) if self.templates else 0,
            'categories': {},
            'components': {},
            'difficulties': {}
        }
        
        # 카테고리 통계
        for tool_name, templates in self.templates.items():
            for template in templates:
                # 카테고리 통계
                category = template.category
                stats['categories'][category] = stats['categories'].get(category, 0) + 1
                
                # 컴포넌트 통계
                component = template.component
                stats['components'][component] = stats['components'].get(component, 0) + 1
                
                # 난이도 통계
                difficulty = template.difficulty
                stats['difficulties'][difficulty] = stats['difficulties'].get(difficulty, 0) + 1
        
        return stats

def main():
    """메인 실행 함수"""
    manager = ToolCallingTemplateManager()
    api_signatures_path = Path("api_signatures.json")
    output_path = Path("tool_calling_templates.json")
    
    # API 시그니처 로드
    manager.load_api_signatures(api_signatures_path)
    
    # 템플릿 생성
    templates = manager.generate_all_templates()
    
    # 템플릿 내보내기
    manager.export_templates(output_path)
    
    # 통계 출력
    stats = manager.get_template_statistics()
    logger.info(f"Template Statistics:")
    logger.info(f"  Total Tools: {stats['total_tools']}")
    logger.info(f"  Total Templates: {stats['total_templates']}")
    logger.info(f"  Categories: {stats['categories']}")
    logger.info(f"  Components: {stats['components']}")
    logger.info(f"  Difficulties: {stats['difficulties']}")

if __name__ == "__main__":
    main()