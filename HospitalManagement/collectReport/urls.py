# collectReport/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.collectReport, name='collectReport'),
    path('reportNotFound/', views.reportNotFound, name='reportNotFound'),
]
