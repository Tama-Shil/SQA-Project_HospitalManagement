from django.urls import path
from . import views

urlpatterns = [
    # Add the URL pattern for the check_patient view
    path('', views.checkPatient, name='check_patient'),
    path('check_patient/', views.checkPatient, name='check_patient'),
    path('patient/dashboard/<str:patient_id>/', views.patientDashboard, name='patient_dashboard'),
    path('patient/submit_selected_medicines/<str:patient_id>/', views.submit_selected_medicines, name='submit_selected_medicines')
  
]
