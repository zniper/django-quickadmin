from distutils.version import StrictVersion

from django import get_version


QADMIN_DEFAULT_EXCLUDES = [
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.comments',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'south',
]

USE_APPCONFIG = not(StrictVersion(get_version()) < StrictVersion('1.7'))
