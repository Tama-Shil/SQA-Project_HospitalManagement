# admin.py

from django.contrib import admin
from .models import Patient  # Import the Patient model

class PatientAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Patient model.

    This class inherits from admin.ModelAdmin to provide additional options
    and customization for the Patient model in the Django admin.
    """

admin.site.register(Patient, PatientAdmin)
"""
Registers the Patient model with the customized PatientAdmin class in the Django admin.

This allows you to manage and interact with Patient objects through the admin interface.
"""
