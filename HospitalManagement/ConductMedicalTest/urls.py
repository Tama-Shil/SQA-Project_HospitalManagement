"""
Module: medical_test_urls

Description:
This module defines URL patterns for the medical test management app.
It specifies the routing configuration for accessing different views related
to conducting medical tests.

URL Patterns:
    - conductMedicalTest: Routes to the view for conducting medical tests.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.conductMedicalTest, name='conductMedicalTest')
]
