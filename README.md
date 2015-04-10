#Django Quick Admin

[![Build Status](https://travis-ci.org/zniper/django-quickadmin.svg)](https://travis-ci.org/zniper/django-quickadmin)
[![Coverage Status](https://coveralls.io/repos/zniper/django-quickadmin/badge.svg?branch=master)](https://coveralls.io/r/zniper/django-quickadmin?branch=master)
[![Downloads](https://pypip.in/download/django-quickadmin/badge.svg)](https://pypi.python.org/pypi/django-quickadmin/)
[![Latest Version](https://pypip.in/version/django-quickadmin/badge.svg)](https://pypi.python.org/pypi/django-quickadmin/)

**django-quickadmin** is a Django application which automatically registers all models found in `INSTALLED_APPS` of settings module. 

*Notice: All models registered to admin via normal method (inside admin.py) will not be affected by this application, they will always show up.*

Installation
------------
The installation process is simple just like most of Django applications, just using `pip` then updating `INSTALLED_APPS`.

    pip install django-quickadmin
  
Locate `INSTALLED_APPS` inside settings file, and put `'django-quickadmin'` there:

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

There you are, just restart the Django instance and visit admin page to see all custom models appeared and ready to be managed.

Configuration
-------------

The application also support very few of customizations, all are placed inside the `settings` module.

* `QADMIN_EXCLUDES` - List of applications or models which will be bypassed/hidden in admin area. In the case below, all undeclared models of `my_first_app` and the model `my_second_app.JustOneModel` will be excluded.
    
        QADMIN_EXCLUDES = [
            'my_first_app',
            'my_second_app.JustOneModel',
        ]

* `QADMIN_EXCLUDE_STOCK` - Option for excluding default/stock applications of Django or not (default = True).

        QADMIN_EXCLUDE_STOCK = False    # models of applications like: south, contenttypes,.. will be shown
