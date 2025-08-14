"""
CLI 통합 테스트 - 오류 처리 및 테스트 모드 검증
"""

import unittest
import tempfile
import os
from pathlib import Path
from click.testing import CliRunner

from cli.main import cli
from cli.error_handler import (
    ErrorHandler, 
    CLIError, 
    ConfigurationError, 
    ValidationError, 
    ResourceError,
    validate_parameters,
    check_system_requirements
)


class TestErrorHandler(unittest.TestCase):
    """오류 처리기 테스트"""
    
    def setUp(self):
        """테스트 설정"""
        self.error_handler = ErrorHandler(verbose=False)
        self.verbose_error_handler = ErrorHandler(verbose=True)
    
    def test_cli_error_handling(self):
        """CLI 오류 처리 테스트"""
        error = CLIError("테스트 오류", suggestions=["해결 방법 1", "해결 방법 2"])
        
        # 예외가 발생하지 않아야 함
        try:
            self.error_handler.handle_exception(error)
        except Exception as e:
            self.fail(f"오류 처리 중 예외 발생: {e}")
    
    def test_configuration_error_handling(self):
        """설정 오류 처리 테스트"""
        error = ConfigurationError("설정 파일이 유효하지 않습니다")
        
        try:
            self.error_handler.handle_exception(error)
        except Exception as e:
            self.fail(f"설정 오류 처리 중 예외 발생: {e}")
    
    def test_validation_error_handling(self):
        """검증 오류 처리 테스트"""
        error = ValidationError("유효하지 않은 파라미터")
        
        try:
            self.error_handler.handle_exception(error)
        except Exception as e:
            self.fail(f"검증 오류 처리 중 예외 발생: {e}")
    
    def test_resource_error_handling(self):
        """리소스 오류 처리 테스트"""
        error = ResourceError("파일을 찾을 수 없습니다")
        
        try:
            self.error_handler.handle_exception(error)
        except Exception as e:
            self.fail(f"리소스 오류 처리 중 예외 발생: {e}")


class TestParameterValidation(unittest.TestCase):
    """파라미터 검증 테스트"""
    
    def test_valid_parameters(self):
        """유효한 파라미터 검증 테스트"""
        # 예외가 발생하지 않아야 함
        validate_parameters(
            steps=["md_processing", "qdrant_search"],
            formats=["sharegpt", "alpaca"],
            target_count=100,
            batch_size=16,
            max_concurrent=4,
            sample_size=10,
            min_quality_score=0.7
        )
    
    def test_invalid_steps(self):
        """유효하지 않은 단계 검증 테스트"""
        with self.assertRaises(ValidationError):
            validate_parameters(steps=["invalid_step"])
    
    def test_invalid_formats(self):
        """유효하지 않은 포맷 검증 테스트"""
        with self.assertRaises(ValidationError):
            validate_parameters(formats=["invalid_format"])
    
    def test_invalid_positive_integers(self):
        """유효하지 않은 양의 정수 검증 테스트"""
        with self.assertRaises(ValidationError):
            validate_parameters(target_count=0)
        
        with self.assertRaises(ValidationError):
            validate_parameters(batch_size=-1)
        
        with self.assertRaises(ValidationError):
            validate_parameters(max_concurrent=0)
        
        with self.assertRaises(ValidationError):
            validate_parameters(sample_size=-5)
    
    def test_invalid_quality_score(self):
        """유효하지 않은 품질 점수 검증 테스트"""
        with self.assertRaises(ValidationError):
            validate_parameters(min_quality_score=-0.1)
        
        with self.assertRaises(ValidationError):
            validate_parameters(min_quality_score=1.1)


class TestSystemRequirements(unittest.TestCase):
    """시스템 요구사항 테스트"""
    
    def test_check_system_requirements(self):
        """시스템 요구사항 확인 테스트"""
        warnings = check_system_requirements()
        
        # 경고 목록이 리스트여야 함
        self.assertIsInstance(warnings, list)
        
        # 각 경고가 문자열이어야 함
        for warning in warnings:
            self.assertIsInstance(warning, str)


if __name__ == "__main__":
    unittest.main()