import io
import sys

import simplejson


def execute_script(file_path):
    with open(file_path) as f:
        script = f.read()

    stdout_backup = sys.stdout
    stdout_redirected = sys.stdout = io.StringIO()
    exec(script)
    sys.stdout = stdout_backup

    return stdout_redirected.getvalue().split('\n')[0]


if __name__ == '__main__':
    print(simplejson.loads(execute_script('weather_tvnmeteo.py')))
