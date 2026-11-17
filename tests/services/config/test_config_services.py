from pathlib import Path

from lexy.services.config.config_services import ConfigServices


def test_load_config(tmp_config_file: Path):
    config = ConfigServices.load_config(tmp_config_file)
    assert config is not None
    assert "editor" in config


def test_change_default_editor(tmp_config_file: Path):
    ConfigServices.change_default_editor("vim", tmp_config_file)
    config = ConfigServices.load_config(tmp_config_file)
    assert config["editor"]["default_editor"] == "vim"
