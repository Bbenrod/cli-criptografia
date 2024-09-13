from setuptools import setup

setup(
    name='cli-criptografia',
    version='0.1',
    packages=['cli'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'crypto=cli.main:cli', 
        ],
    },
)
