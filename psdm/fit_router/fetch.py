import json
import requests


def download_repo_files():
    with open('./repo_files.json') as config:
        files = dict([(file['filename'], file['url']) for file in json.load(config)['files']])
        for name in files:
            response = requests.get(files[name])
            response.encoding = 'utf-8'
            with open('../_repo/{0}'.format(name), 'w') as file:
                file.write(response.text)
