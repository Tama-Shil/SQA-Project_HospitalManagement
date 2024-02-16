from django.urls import path
from .views import ambulance_call_form, ambulance_dispatch

app_name = 'call_ambulance'

urlpatterns = [
    path('call-form/', ambulance_call_form, name='call_form'),
    path('dispatch/', ambulance_dispatch, name='dispatch'),
    # Add more URLs as needed
]
