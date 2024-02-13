from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.form_page,name='form_page'),
    path('savePatientData/', views.savePatientData, name = 'savePatientData'),
    path('patient_admission_success/', views.patient_admission_success, name='patient_admission_success')
]

