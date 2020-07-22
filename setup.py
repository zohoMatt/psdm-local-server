from setuptools import setup, find_packages

setup(
    name='PSDM Local Server',
    version='0.1',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask'],

    author='MattZuo',
    author_email='mattzuo12@gmail.com',
    description='Local server compiled to binary executable in order to be integrated into Electron app.',
    keywords='flask python server',
    url='https://github.com/zohoMatt/psdm-local-server',
    project_urls={
        'Bug Tracker': 'https://github.com/zohoMatt/psdm-local-server/issues',
        'Documentation': 'https://github.com/zohoMatt/psdm-local-server/blob/master/README.md',
        'Source Code': 'https://github.com/zohoMatt/psdm-local-server',
    },
    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License'
    ]
)