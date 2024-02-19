"""
Module: urls

This module defines URL patterns for the entire project.

"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('prescription/', include('PrescribePatient.urls')),
    path('conductMedicalTest/',include('ConductMedicalTest.urls'))   
]