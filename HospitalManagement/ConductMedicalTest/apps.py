"""
Module: apps

Description:
This module defines the configuration for the ConductMedicalTest app.

Classes:
    - ConductMedicalTestConfig: Configuration class for the ConductMedicalTest app.
"""

from django.apps import AppConfig

class ConductMedicalTestConfig(AppConfig):
    """
    Configuration class for the ConductMedicalTest app.

    Inherits from:
        AppConfig

    Attributes:
        default_auto_field (str): The default auto field to use for models.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ConductMedicalTest'
