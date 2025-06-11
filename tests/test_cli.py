import subprocess
import sys
import pytest
from ai_coder.cli import main

def test_help_exit_code():
    result = subprocess.run([sys.executable, '-m', 'ai_project.cli', '--help'])
    assert result.returncode == 0

def test_main_returns_none(capsys):
    assert main() is None
    captured = capsys.readouterr()
    assert "Welcome to AI Project Maker!" in captured.out