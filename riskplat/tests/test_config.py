"""Tests for Riskplat application configuration."""

import pytest
from pydantic import ValidationError

from riskplat.core.config import Settings


def test_default_settings() -> None:
    """Settings should have valid default values."""
    config = Settings(_env_file=None)

    assert config.app_name == "Riskplat"
    assert config.environment == "development"
    assert config.debug is False
    assert config.api_prefix == "/api/v1"
    assert config.log_level == "INFO"
    assert config.database_url is None


def test_settings_accept_valid_environment() -> None:
    """Settings should accept supported environment values."""
    config = Settings(
        _env_file=None,
        environment="testing",
        debug=True,
        log_level="DEBUG",
    )

    assert config.environment == "testing"
    assert config.debug is True
    assert config.log_level == "DEBUG"


def test_settings_reject_invalid_environment() -> None:
    """Settings should reject unsupported environment values."""
    with pytest.raises(ValidationError):
        Settings(_env_file=None, environment="invalid")


def test_settings_reject_invalid_log_level() -> None:
    """Settings should reject unsupported log levels."""
    with pytest.raises(ValidationError):
        Settings(_env_file=None, log_level="INVALID")
