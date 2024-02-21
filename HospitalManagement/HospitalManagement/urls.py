# HospitalManagement/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Admin interface URL
    
    path('', views.home, name='home'),
    # Home page URL
    
    path('admission/', include("getAdmitted.urls")),
    # Include URLs from the 'getAdmitted' app under the 'admission/' path
    
    path('report/', include("collectReport.urls"))
    # Include URLs from the 'collectReport' app under the 'report/' path
]
