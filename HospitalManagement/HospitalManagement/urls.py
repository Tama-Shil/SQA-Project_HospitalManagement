
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('payment/',include("App_Payment.urls")),
    path('discharge/',include("App_DischargePatient.urls")),
]

