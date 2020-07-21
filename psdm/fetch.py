import json
import requests
from os import path


def download_repo_files():
    env = path.dirname(__file__)
    print('>>> Downloading latest model...')
    with open(path.join(env, './_repo/repo_files.json')) as config:
        files = dict([(file['filename'], file['url']) for file in json.load(config)['files']])
        for name in files:
            response = requests.get(files[name])
            response.encoding = 'utf-8'
            with open(path.join(env, './_repo/{0}'.format(name)), 'w') as file:
                file.write(response.text)
                print('>>> Succeed in downloading {0}'.format(name))
