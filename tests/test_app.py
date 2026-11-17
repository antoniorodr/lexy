from click.testing import CliRunner

from lexy.lexy import lexy


def test_lexy_help(app: CliRunner):
    result = app.invoke(lexy, ["--help"])
    assert result.exit_code == 0


def test_lexy_modified_command(app: CliRunner):
    result = app.invoke(lexy, ["modified"])
    assert result.exit_code == 0
