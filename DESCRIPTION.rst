.. image:: https://travis-ci.org/zniper/django-quickadmin.svg?branch=master
    :target: https://travis-ci.org/zniper/django-quickadmin

.. image:: https://coveralls.io/repos/zniper/django-quickadmin/badge.svg?branch=master 
    :target: https://coveralls.io/r/zniper/django-quickadmin?branch=master


This is a small Django application which automatically registers all found models withtin the current project into the admin area.

Features
========

* Add all found models from other installed applications into admin section
* Configurable exclusion of specific applications and models
* Auto exclude models from stock applications of Django

Installation
============

To install the latest release, just using pip::

    pip install django-quickadmin

Then insert 'quickadmin' into INSTALLED_APPS inside settings module::

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        ...
        'quickadmin',
        ...
    )

For any questions or comments regarding this application, please email to me[at]zniper.net.
