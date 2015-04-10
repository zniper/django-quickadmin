from .config import USE_APPCONFIG

if USE_APPCONFIG:
    default_app_config = 'quickadmin.apps.QAdminAppConfig'
else:
    from .register import register_models
    register_models()
