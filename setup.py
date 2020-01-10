'''Setup.py'''

from distutils.core import setup
from setuptools import find_packages

setup(
    name='target',
    version='0.0.0',
    author='Nicholas McKibben',
    author_email='nicholas.bgp@gmail.com',
    packages=find_packages(),
    scripts=[],
    url='https://github.com/backupinator/target',
    license='GPLv3',
    description='App running on target machine holding backups.',
    long_description=open('README.rst').read(),
    install_requires=[
    ],
    python_requires='>=3.6',
)
