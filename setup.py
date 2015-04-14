from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-quickadmin',
    version='0.1.1',
    description='Django application automatically registers all found models into admin area',
    long_description=long_description,
    url='https://github.com/zniper/django-quickadmin',
    author='Ha Pham',
    author_email='me.zniper@gmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='django admin models register python',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[''],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)
