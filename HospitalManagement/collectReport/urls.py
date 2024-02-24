# collectReport/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL for collecting a report
    path('', views.collectReport, name='collectReport'),

    # URL for reporting not found
    path('reportNotFound/', views.reportNotFound, name='reportNotFound'),
]
