import pytest
from typer.testing import CliRunner

from pyfsolver.cli import app

runner = CliRunner()


@pytest.mark.cli
@pytest.mark.integration
def test_version():
    result = runner.invoke(app, "--version")

    assert result.exit_code == 0
    assert "pyfsolver 0.1.0" in result.stdout


@pytest.mark.cli
@pytest.mark.integration
def test_cli():
    result = runner.invoke(app)

    assert result.exit_code == 0
    assert "Usage: pyfsolver [OPTIONS] COMMAND [ARGS] ..." in result.stdout


@pytest.mark.cli
@pytest.mark.integration
def test_fortran_run():
    result = runner.invoke(app, ["fortran", "tests/coo_files/sist3.mtx", "tests/coo_files/sist3_b.mtx"])

    assert result.exit_code == 0


@pytest.mark.cli
@pytest.mark.integration
def test_fortran_run_print_option():
    result = runner.invoke(app, ["numpy", "tests/coo_files/sist3.mtx", "tests/coo_files/sist3_b.mtx"])
    assert result.exit_code == 0
