#setup.py

from setuptools import setup
setup(
    name='gymondo',
    version='0.0.1',
    py_modules=['yourscript'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'gymondo=gymondo:main'
        ]
    }
)