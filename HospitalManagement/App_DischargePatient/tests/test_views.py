# hospital_management_app/tests/test_views.py
from django.test import RequestFactory
from django.urls import reverse
from App_DischargePatient.models import Patient
from App_DischargePatient.views import dischargePatient
import pytest

@pytest.mark.django_db
def test_discharge_patient_view_payment_paid():
    patient = Patient.objects.create(
        name="John Doe",
        patientId="P001",
        gender="M",
        cabinNo="C001",
        totalBill=1000,
        paymentPaid=True  # Assume payment is already paid for this patient
    )
    request = RequestFactory().post(reverse('discharge_patient'), {'patientId': 'P001'})
    response = dischargePatient(request)
    assert response.status_code == 200
    assert b'patient' in response.content

"""
@pytest.mark.django_db
def test_discharge_patient_view_payment_not_paid():
    patient = Patient.objects.create(
        name="Jane Doe",
        patientId="P002",
        gender="F",
        cabinNo="C002",
        totalBill=1500,
        paymentPaid=False
    )
    request = RequestFactory().post(reverse('discharge_patient'), {'patientId': 'P002'})
    response = dischargePatient(request)
    assert response.status_code == 200
    assert b'paymentDue' in response.content
"""
