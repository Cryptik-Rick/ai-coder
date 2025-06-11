import subprocess
import sys

def test_echo():
    result = subprocess.run([sys.executable, '-m', 'ai_coder.cli', 'hello'], capture_output=True, text=True)
    assert 'hello' in result.stdout