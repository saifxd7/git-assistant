import subprocess
import logging

def get_git_diff():
    try:
        result = subprocess.run(['git', 'diff', '--staged'], stdout=subprocess.PIPE, check=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to get git diff: {e}")
        return None