import subprocess
from os import path


def run_cmd(cmd):
    return subprocess.Popen(cmd.split()).wait()


# Clean directories
run_cmd('rm -rf build')
run_cmd('rm -rf dist')
run_cmd('rm __init__.spec')

# First run
run_cmd('python ./scripts/fetch.py')
try:
    run_cmd('pyinstaller --additional-hooks-dir=./scripts/hooks --onefile ./psdm/__init__.py')
except:
    print('>>> First-time package ends')

# Modify file
RAW = 'hiddenimports=[]'
MODIFIED = "hiddenimports=['pkg_resources.py2_warn']"
IMPORTS = 'import sys\nsys.setrecursionlimit(5000)\n'

print('>>> Start second-time package')
print(path.getsize('__init__.spec'))
with open('__init__.spec', 'r+') as file:
    raw = file.read()

    print('File content: ', raw)
    file.seek(0)
    file.write(IMPORTS + raw.replace(RAW, MODIFIED))
    file.truncate()

run_cmd('pyinstaller --onefile ./__init__.spec')
