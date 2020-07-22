import json
import requests
from os import path

OLD_IMPORT = 'from PSDM_functions import *'
NEW_IMPORT = 'from psdm.fit_router.repo.PSDM_functions import *'


def download_repo_files():
    env = path.dirname(__file__)
    print('>>> Downloading latest model...')
    with open(path.join(env, './fit_router/repo/repo_files.json')) as config:
        files = dict([(file['filename'], file['url']) for file in json.load(config)['files']])
        for name in files:
            response = requests.get(files[name])
            response.encoding = 'utf-8'
            with open(path.join(env, './fit_router/repo/{0}'.format(name)), 'w') as file:
                file.write(response.text.replace(OLD_IMPORT, NEW_IMPORT))
                print('>>> Succeed in downloading {0}'.format(name))
