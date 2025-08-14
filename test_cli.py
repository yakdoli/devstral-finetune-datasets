"""
CLI 인터페이스 단위 테스트
"""

import unittest
from click.testing import CliRunner
from pathlib import Path
import tempfile
import os

from cli.main import cli, validate_steps, validate_formats, validate_positive_int, validate_float_range


class TestCLIValidators(unittest.TestCase):
    """CLI 검증 함수 테스트"""
    
    def test_validate_steps_valid(self):
        """유효한 파이프라인 단계 검증 테스트"""
        # 단일 단계
        result = validate_steps(None, None, "md_processing")
        self.assertEqual(result, ["md_processing"])
        
        # 다중 단계
        result = validate_steps(None, None, "md_processing,qdrant_search,conversation_generation")
        self.assertEqual(result, ["md_processing", "qdrant_search", "conversation_generation"])
        
        # 공백 포함
        result = validate_steps(None, None, " md_processing , qdrant_search ")
        self.assertEqual(result, ["md_processing", "qdrant_search"])
        
        # None 값
        result = validate_steps(None, None, None)
        self.assertIsNone(result)
    
    def test_validate_steps_invalid(self):
        """유효하지 않은 파이프라인 단계 검증 테스트"""
        from click import BadParameter
        
        with self.assertRaises(BadParameter) as context:
            validate_steps(None, None, "invalid_step")
        self.assertIn("유효하지 않은 단계", str(context.exception))
        
        with self.assertRaises(BadParameter) as context:
            validate_steps(None, None, "md_processing,invalid_step")
        self.assertIn("유효하지 않은 단계", str(context.exception))
    
    def test_validate_formats_valid(self):
        """유효한 출력 포맷 검증 테스트"""
        # 단일 포맷
        result = validate_formats(None, None, "sharegpt")
        self.assertEqual(result, ["sharegpt"])
        
        # 다중 포맷
        result = validate_formats(None, None, "sharegpt,alpaca,openai")
        self.assertEqual(result, ["sharegpt", "alpaca", "openai"])
        
        # None 값
        result = validate_formats(None, None, None)
        self.assertIsNone(result)
    
    def test_validate_formats_invalid(self):
        """유효하지 않은 출력 포맷 검증 테스트"""
        from click import BadParameter
        
        with self.assertRaises(BadParameter) as context:
            validate_formats(None, None, "invalid_format")
        self.assertIn("유효하지 않은 포맷", str(context.exception))
    
    def test_validate_positive_int_valid(self):
        """양의 정수 검증 테스트 - 유효한 값"""
        result = validate_positive_int(None, None, 10)
        self.assertEqual(result, 10)
        
        result = validate_positive_int(None, None, 1)
        self.assertEqual(result, 1)
        
        result = validate_positive_int(None, None, None)
        self.assertIsNone(result)
    
    def test_validate_positive_int_invalid(self):
        """양의 정수 검증 테스트 - 유효하지 않은 값"""
        from click import BadParameter
        
        with self.assertRaises(BadParameter):
            validate_positive_int(None, None, 0)
        
        with self.assertRaises(BadParameter):
            validate_positive_int(None, None, -1)
    
    def test_validate_float_range_valid(self):
        """실수 범위 검증 테스트 - 유효한 값"""
        validator = validate_float_range(0.0, 1.0)
        
        result = validator(None, None, 0.5)
        self.assertEqual(result, 0.5)
        
        result = validator(None, None, 0.0)
        self.assertEqual(result, 0.0)
        
        result = validator(None, None, 1.0)
        self.assertEqual(result, 1.0)
        
        result = validator(None, None, None)
        self.assertIsNone(result)
    
    def test_validate_float_range_invalid(self):
        """실수 범위 검증 테스트 - 유효하지 않은 값"""
        from click import BadParameter
        
        validator = validate_float_range(0.0, 1.0)
        
        with self.assertRaises(BadParameter):
            validator(None, None, -0.1)
        
        with self.assertRaises(BadParameter):
            validator(None, None, 1.1)


class TestCLICommands(unittest.TestCase):
    """CLI 명령어 테스트"""
    
    def setUp(self):
        """테스트 설정"""
        self.runner = CliRunner()
    
    def test_cli_help(self):
        """CLI 도움말 테스트"""
        result = self.runner.invoke(cli, ["--help"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Unsloth Dataset Generator", result.output)
        self.assertIn("Syncfusion WinForms", result.output)
    
    def test_generate_help(self):
        """generate 명령어 도움말 테스트"""
        result = self.runner.invoke(cli, ["generate", "--help"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("데이터셋 생성 파이프라인 실행", result.output)
        self.assertIn("--config", result.output)
        self.assertIn("--steps", result.output)
        self.assertIn("--test-mode", result.output)
    
    def test_generate_dry_run(self):
        """generate 명령어 드라이 런 테스트"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write("test: config")
            config_path = f.name
        
        try:
            result = self.runner.invoke(cli, [
                "generate", 
                "--config", config_path,
                "--dry-run"
            ])
            self.assertEqual(result.exit_code, 0)
            self.assertIn("드라이 런 모드", result.output)
        finally:
            os.unlink(config_path)
    
    def test_generate_invalid_steps(self):
        """generate 명령어 유효하지 않은 단계 테스트"""
        result = self.runner.invoke(cli, [
            "generate",
            "--steps", "invalid_step"
        ])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("유효하지 않은 단계", result.output)
    
    def test_generate_invalid_formats(self):
        """generate 명령어 유효하지 않은 포맷 테스트"""
        result = self.runner.invoke(cli, [
            "generate",
            "--formats", "invalid_format"
        ])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("유효하지 않은 포맷", result.output)
    
    def test_generate_invalid_positive_int(self):
        """generate 명령어 유효하지 않은 양의 정수 테스트"""
        result = self.runner.invoke(cli, [
            "generate",
            "--target-count", "0"
        ])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("양의 정수여야 합니다", result.output)
    
    def test_generate_invalid_quality_score(self):
        """generate 명령어 유효하지 않은 품질 점수 테스트"""
        result = self.runner.invoke(cli, [
            "generate",
            "--min-quality-score", "1.5"
        ])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("사이의 값이어야 합니다", result.output)
    
    def test_validate_config_nonexistent(self):
        """validate-config 명령어 존재하지 않는 파일 테스트"""
        result = self.runner.invoke(cli, [
            "validate-config",
            "--config", "nonexistent.yaml"
        ])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("찾을 수 없습니다", result.output)
    
    def test_list_steps(self):
        """list-steps 명령어 테스트"""
        result = self.runner.invoke(cli, ["list-steps"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("파이프라인 단계", result.output)
        self.assertIn("md_processing", result.output)
        self.assertIn("qdrant_search", result.output)
        self.assertIn("conversation_generation", result.output)
    
    def test_list_formats(self):
        """list-formats 명령어 테스트"""
        result = self.runner.invoke(cli, ["list-formats"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("출력 포맷", result.output)
        self.assertIn("sharegpt", result.output)
        self.assertIn("alpaca", result.output)
        self.assertIn("openai", result.output)
    
    def test_version(self):
        """version 명령어 테스트"""
        result = self.runner.invoke(cli, ["version"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("버전", result.output)
        # Rich 포맷팅으로 인해 버전이 분리될 수 있으므로 개별적으로 확인
        self.assertIn("1.0", result.output)
        self.assertIn("0", result.output)


class TestCLIIntegration(unittest.TestCase):
    """CLI 통합 테스트"""
    
    def setUp(self):
        """테스트 설정"""
        self.runner = CliRunner()
    
    def test_generate_with_all_options(self):
        """모든 옵션을 포함한 generate 명령어 테스트"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write("test: config")
            config_path = f.name
        
        try:
            result = self.runner.invoke(cli, [
                "generate",
                "--config", config_path,
                "--steps", "md_processing,qdrant_search",
                "--formats", "sharegpt,alpaca",
                "--target-count", "100",
                "--batch-size", "16",
                "--max-concurrent", "4",
                "--test-mode",
                "--sample-size", "5",
                "--verbose",
                "--log-level", "DEBUG",
                "--min-quality-score", "0.7",
                "--dry-run"
            ])
            self.assertEqual(result.exit_code, 0)
            self.assertIn("실행 설정", result.output)
            self.assertIn("드라이 런 모드", result.output)
        finally:
            os.unlink(config_path)


if __name__ == "__main__":
    unittest.main()