# make_appointment/urls.py
from django.urls import path
from .views import make_appointment, appointment_success

urlpatterns = [
    path('', make_appointment, name='make_appointment'),
    path('success/', appointment_success, name='appointment_success'),
]
