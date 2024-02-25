
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('call_ambulance/', include('call_ambulance.urls')),
    path('call-form/', include('call_ambulance.urls')),
    path('dispatch/', include('call_ambulance.urls')),
    path('make_appointment/', include('make_appointment.urls')),
]

#views.home, name='home'