from django.contrib import admin
from django.utils.module_loading import import_module
from django.db.models import get_models
from django.conf import settings
from django.conf.urls import include, url

from django.utils.log import getLogger

from .config import QADMIN_DEFAULT_EXCLUDES, USE_APPCONFIG


logger = getLogger(__name__)

# This have to be run first, to init the url set
project_urls = import_module(settings.ROOT_URLCONF)

EXCL_MODELS = len('.models')


def filter_models(exclude=None):
    """Returns all found models within this Django instance"""
    # Get all the models from installed apps
    model_list = []
    if USE_APPCONFIG:
        from django.apps import apps
        found = apps.get_models()
    else:
        found = get_models()

    # Exclude some models
    excl_set = list(getattr(settings, 'QADMIN_EXCLUDES', []))
    if getattr(settings, 'QADMIN_EXCLUDE_STOCK', True):
        excl_set.extend(QADMIN_DEFAULT_EXCLUDES)
    for model in found:
        app_name = model.__module__[:-EXCL_MODELS]
        full_name = '.'.join([app_name, model.__name__])
        if full_name in excl_set or app_name in excl_set:
            continue
        model_list.append(model)
    return model_list


def update_admin_urls():
    """Admin urls set have to be updated or all new registered models will
    be shown as disabled in admin area"""
    # Delete the old admin URLs
    old_pattern = None
    admin_regex = r'^admin/'
    for url_item in project_urls.urlpatterns:
        if url_item.app_name == 'admin':
            old_pattern = url_item
            admin_regex = url_item.regex.pattern
            project_urls.urlpatterns.remove(url_item)
            break
    # Reload updated admin URLs
    try:
        admin.autodiscover()
        project_urls.urlpatterns.append(
            url(admin_regex, include(admin.site.urls))
        )
    except:
        logger.error('Error when updating new admin urls.')
        if old_pattern:
            project_urls.urlpatterns.append(old_pattern)


def register_models():
    """Register all models insde specific application"""
    for model in filter_models():
        try:
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            logger.error('The model "%s" is already registered' %
                         model.__name__)
    update_admin_urls()
