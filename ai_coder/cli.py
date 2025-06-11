import argparse
import subprocess
import sys
from ai_coder.logging_config import get_logger

def init_project():
    # Placeholder for project initialization logic
    pass

def main():
    parser = argparse.ArgumentParser(prog='ai-project')
    parser.add_argument('--version', action='version', version='0.1.0')
    args = parser.parse_args()
    print("Welcome to AI Project Maker!")
    init_project()

def test_cli_prints_version():
    result = subprocess.run([
        sys.executable, '-m', 'ai_coder.cli', '--version'
    ], capture_output=True, text=True)
    assert result.returncode == 0
    assert '0.1.0' in result.stdout


def test_cli_prints_welcome_on_run():
    result = subprocess.run([
        sys.executable, '-m', 'ai_coder.cli'
    ], capture_output=True, text=True)
    assert result.returncode == 0
    assert 'Welcome to AI Project Maker!' in result.stdout

if __name__ == '__main__':
    main()