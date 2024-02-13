from django.urls import path
from .views import advancePayment, selectPaymentMethod,  emiPayment

urlpatterns = [
    path('', selectPaymentMethod, name='select_payment_method'),
    path('PayBill/', advancePayment, name='advance_payment_form'),
    path('emiPayment/', emiPayment, name='emi_payment_form'),
]