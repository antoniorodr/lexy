import click
import pytest
import sys
from unittest.mock import MagicMock, mock_open, patch

from click.testing import CliRunner

from lexy.lexy import lexy


def _base_mocks(MockScraper, MockInit):
    mock_scraper = MockScraper.return_value
    mock_scraper.auto_update = MagicMock()
    mock_scraper.json_path = "/test/path"
    MockInit.return_value.ensure_languages_file = MagicMock()
    return mock_scraper


FAKE_JSON = '[{"language": "Python", "language_url": "http://x", "language_file_url": "http://x/py", "file_extension": ".py"}]'


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def lexy_mocks():
    with (
        patch("lexy.lexy.LexyScraper") as MockScraper,
        patch("lexy.lexy.LexyInit") as MockInit,
        patch("lexy.lexy.LexyFinder") as MockFinder,
        patch("builtins.open", mock_open(read_data=FAKE_JSON)),
    ):
        yield _base_mocks(MockScraper, MockInit), MockFinder.return_value


def test_lexy(runner, lexy_mocks):
    _, finder = lexy_mocks
    finder.language_finder = MagicMock()
    result = runner.invoke(lexy, ["python"])
    assert result.exit_code == 0


def test_lexy_with_invalid_language(runner, lexy_mocks):
    def fake_language_finder(lang):
        click.secho(f"Language {lang} not found", fg="red")
        sys.exit(1)

    _, finder = lexy_mocks
    finder.language_finder = fake_language_finder
    result = runner.invoke(lexy, ["invalid_language"])
    assert result.exit_code == 1
    assert "not found" in result.output


def test_lexy_with_modified(runner, lexy_mocks):
    scraper, _ = lexy_mocks
    scraper.last_modified.return_value = "12.03.2026"
    result = runner.invoke(lexy, ["modified"])
    assert result.exit_code == 0
    assert "The most recent update to Lexy was on:" in result.output


def test_lexy_list(runner, lexy_mocks):
    _, finder = lexy_mocks
    finder.get_language = MagicMock()
    result = runner.invoke(lexy, ["list"])
    assert result.exit_code == 0
