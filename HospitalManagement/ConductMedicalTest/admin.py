"""
Module: admin

Description:
This module registers the TestRecord model with the Django admin interface.

Functions:
    - registerTestRecord: Registers the TestRecord model with the Django admin interface.
"""

from django.contrib import admin
from .models import TestRecord

def registerTestRecord():
    """
    Registers the TestRecord model with the Django admin interface.
    """
    admin.site.register(TestRecord)
