"""
URL Configuration
-----------------

This module defines URL patterns for the App_Payment application.

"""
from django.urls import path
from .views import selectPaymentMethod,paymentSuccess

urlpatterns = [
    path('', selectPaymentMethod, name='select_payment_method'),
    path('paymentSuccess/', paymentSuccess, name='paymentSuccess'),
    
    
]