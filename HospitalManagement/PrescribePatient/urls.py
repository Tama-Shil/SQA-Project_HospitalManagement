"""
Module: urls

This module defines URL patterns for the PrescribePatient app.

"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.prescribePatient, name='prescribePatient')
]
