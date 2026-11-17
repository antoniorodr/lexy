import shutil
import types

import pytest
from click.testing import CliRunner

from lexy.services.config.config_services import ConfigServices


@pytest.fixture
def app() -> types.GeneratorType:
    lexy_app = CliRunner()
    yield lexy_app


@pytest.fixture
def tmp_config_file(tmp_path) -> types.GeneratorType:
    original_path = ConfigServices.create_config_file()
    test_path = tmp_path / "config.toml"
    shutil.copy(original_path, test_path)
    yield test_path
