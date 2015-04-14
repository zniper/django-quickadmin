import os
import sys

import django

from django.conf import settings


current_dir = os.path.dirname(os.path.realpath(__file__))

settings.configure(
    DEBUG=True,
    USE_TZ=True,
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        }
    },
    ROOT_URLCONF="quickadmin.urls",
    INSTALLED_APPS=[
        "django.contrib.auth",
        "django.contrib.admin",
        "django.contrib.contenttypes",
        "django.contrib.sites",
        "django.contrib.sessions",
        "quickadmin",
    ],
    MIDDLEWARE_CLASSES=(
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        ),
    SITE_ID=1,
    TEMPLATE_DIRS=[
        os.path.abspath(os.path.join(os.path.dirname(__file__), "quickadmin", "tests", "templates")),
    ],
)


if hasattr(django, "setup"):
    django.setup()

from django_nose import NoseTestSuiteRunner

test_runner = NoseTestSuiteRunner(verbosity=1)
failures = test_runner.run_tests(["quickadmin"])

if failures:
    sys.exit(failures)
