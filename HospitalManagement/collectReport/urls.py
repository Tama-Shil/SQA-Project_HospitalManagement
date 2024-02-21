from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.submitReport, name='submitReport'), 
    path('report/', views.submitReport, name='submitReport'),
    # Add other URL patterns as needed
]
