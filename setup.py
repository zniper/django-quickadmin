# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='quickadmin',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.1',

    description='Django application support quick adding models management into admin area',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/zniper/django-quickadmin',

    # Author details
    author='Ha Pham',
    author_email='me.zniper@gmail.com',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='django admin models customize list python',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=[''],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)
