# urls.py

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.formPage, name='formPage'),  
    # URL for displaying the patient admission form

    path('savePatientData/', views.savePatientData, name='savePatientData'),  
    # URL for handling the form submission and saving patient data

    path('patientAdmissionSuccess/', views.patientAdmissionSuccess, name='patientAdmissionSuccess'),  
    # URL for displaying a success page after successful patient admission
]