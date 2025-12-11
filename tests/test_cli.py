import pytest
from subprocess import run, PIPE

def test_cli_help():
    result = run(["python", "-m", "src.cli", "--help"], stdout=PIPE, stderr=PIPE, text=True)
    assert "AGAT: Genome Analysis Toolkit" in result.stdout