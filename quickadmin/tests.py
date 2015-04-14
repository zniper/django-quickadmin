from django.test import TestCase
from django.contrib.auth.models import Permission, User, Group
from django.conf import settings
from django.db.models import get_models
from django.utils.module_loading import import_module

try:
    from django.test import override_settings
except ImportError:
    from django.test.utils import override_settings

from quickadmin import register


class FilterModelTestCase(TestCase):

    @override_settings(QADMIN_EXCLUDES=[], QADMIN_EXCLUDE_STOCK=False)
    def test_filter_models(self):
        """Nothing will be excluded, all models returned as is"""
        models = register.filter_models()
        self.assertEqual(models, get_models())
        self.assertIn(Permission, models)

    @override_settings(QADMIN_EXCLUDES=[], QADMIN_EXCLUDE_STOCK=True)
    def test_filter_exclude_stock(self):
        models = register.filter_models()
        self.assertNotEqual(models, get_models())

    @override_settings(QADMIN_EXCLUDES=['django.contrib.auth.Permission'],
                       QADMIN_EXCLUDE_STOCK=False)
    def test_filter_exclude_model(self):
        models = register.filter_models()
        self.assertNotEqual(models, get_models())
        self.assertNotIn(Permission, models)

    @override_settings(QADMIN_EXCLUDES=['django.contrib.auth'],
                       QADMIN_EXCLUDE_STOCK=False)
    def test_filter_exclude_app(self):
        models = register.filter_models()
        self.assertNotEqual(models, get_models())
        self.assertNotIn(Permission, models)
        self.assertNotIn(User, models)
        self.assertNotIn(Group, models)


class UpdateURLTestCase(TestCase):

    def test_update_urls(self):
        """Simple check for number of items in URLconf"""
        urls = import_module(settings.ROOT_URLCONF)
        org_len = len(urls.urlpatterns)
        register.update_admin_urls()
        self.assertEqual(org_len, len(urls.urlpatterns))
