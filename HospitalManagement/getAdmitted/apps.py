# apps.py

from django.apps import AppConfig

class GetAdmittedConfig(AppConfig):
    """
    AppConfig class for the 'getAdmitted' Django app.

    This class configures the 'getAdmitted' app, including the default_auto_field setting and the app name.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    """
    Specifies the default auto field for models in the 'getAdmitted' app.
    """

    name = 'getAdmitted'
    """
    Specifies the name of the 'getAdmitted' app, which is used to uniquely identify the app within the Django Project.
    """
