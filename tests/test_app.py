from typer.testing import CliRunner

from aoc.cli import app

runner = CliRunner()

def test_app():
    result = runner.invoke(app, ["one"])
    assert result.exit_code == 2
