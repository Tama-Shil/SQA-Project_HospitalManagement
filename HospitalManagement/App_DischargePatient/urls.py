from django.urls import path
from .views import dischargePatient
urlpatterns = [
    #path('', check_payment, name='check_payment'),
    #path('patient_detail/<str:patient_id>/', patient_detail, name='patient_detail'),
    #path('', selectPaymentMethod, name='select_payment_method'),
    path('', dischargePatient, name='discharge_patient'),

]
