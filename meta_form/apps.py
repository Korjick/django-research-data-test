import pluggy
from django.apps import AppConfig

from meta_form import pluggy_specs, pluggy_lib, app_name
from meta_form.pluggy_specs import plugin_manager


class MetaFormConfig(AppConfig):
    verbose_name = 'MetaForm App'
    default_auto_field = 'django.db.models.BigAutoField'
    name = app_name

    def ready(self):
        plugin_manager.add_hookspecs(pluggy_specs)
        plugin_manager.load_setuptools_entrypoints(app_name)
        plugin_manager.register(pluggy_lib)
