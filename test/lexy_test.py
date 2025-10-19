from click.testing import CliRunner
from lexy.lexy import lexy
from unittest.mock import patch, MagicMock, mock_open

def test_lexy():
    runner = CliRunner()
    result = runner.invoke(lexy, ["python"])
    assert result.exit_code == 0


def test_lexy_with_invalid_language():
    runner = CliRunner()
    result = runner.invoke(lexy, ["invalid_language"])
    assert result.exit_code == 1
    assert "not found" in result.output

def test_lexy_with_modified():
    runner = CliRunner()
    result = runner.invoke(lexy, ["modified"])
    assert result.exit_code == 0
    assert "The most recent update to Lexy was on:" in result.output

def test_lexy_list():
    runner = CliRunner()
    fake_json = '{"python": {}, "java": {}}'
    with patch("lexy.lexy.lexy_scraper") as mock_scraper, patch("lexy.lexy.LexyInit") as MockInit, \
         patch("lexy.lexy.LexyFinder") as MockFinder,patch("builtins.open", mock_open(read_data=fake_json)):
        mock_scraper.json_path = "/test/path"
        mock_scraper.auto_update = MagicMock()
        MockInit.return_value.ensure_languages_file = MagicMock()
        mock_finder = MockFinder.return_value
        mock_finder.get_language = MagicMock()
        result = runner.invoke(lexy, ["list"])
        assert result.exit_code == 0
