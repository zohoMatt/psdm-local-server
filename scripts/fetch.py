import requests
from os import path

OLD_IMPORT = 'from PSDM_functions import *'
NEW_IMPORT = 'from psdm.fit_router.repo.PSDM_functions import *'
SOURCE_FILES = {
    'files': [
        {
            'filename': 'PSDM.py',
            'url': 'https://raw.githubusercontent.com/USEPA/Water_Treatment_Models/master/PSDM/PSDM.py'
        },
        {
            'filename': 'PSDM_functions.py',
            'url': 'https://raw.githubusercontent.com/USEPA/Water_Treatment_Models/master/PSDM/PSDM_functions.py'
        }
    ]
}


def download_repo_files():
    env = path.dirname(__file__)
    print('>>> Downloading latest model...')
    files = dict([(file['filename'], file['url']) for file in SOURCE_FILES['files']])
    for name in files:
        response = requests.get(files[name])
        response.encoding = 'utf-8'
        with open(path.join(env, '../psdm/fit_router/repo/{0}'.format(name)), 'w') as file:
            file.write(response.text.replace(OLD_IMPORT, NEW_IMPORT))
            print('>>> Succeed in downloading {0}'.format(name))


if __name__ == '__main__':
    download_repo_files()
