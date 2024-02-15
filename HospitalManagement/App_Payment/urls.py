"""
URL Configuration
-----------------

This module defines URL patterns for the App_Payment application.

"""
from django.urls import path
from .views import selectPaymentMethod

urlpatterns = [
    path('', selectPaymentMethod, name='select_payment_method'),
]