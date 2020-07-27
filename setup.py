from setuptools import setup
setup(
    name = 'KTcli-test',
    version = '0.1.0',
    packages = ['KTcloud'],
    entry_points = {
        'console_scripts': [
            'KTcloud = KTcloud.__main__:main'
        ]
    })