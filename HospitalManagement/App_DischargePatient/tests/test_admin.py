import pytest
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from django.test import Client
from ..models import Patient
from django.urls import reverse
from ..admin import PatientAdmin
@pytest.mark.django_db
def test_patient_admin_list_display():
    # Create a test user
    user = User.objects.create_superuser(username='admin', email='admin@example.com', password='admin')

    # Create a client and log the user in
    client = Client()
    client.force_login(user)

    # Create a Patient object
    patient = Patient.objects.create(name='John Doe', patientId='P001', gender='M', cabinNo='C001', totalBill=1000, paymentPaid=True)

    # Create an instance of the PatientAdmin
    patient_admin = PatientAdmin(Patient, AdminSite())

    # Get the list display fields
    list_display = patient_admin.get_list_display(None)

    # Check if list_display contains the expected fields
    assert 'name' in list_display
    assert 'patientId' in list_display
    assert 'gender' in list_display
    assert 'cabinNo' in list_display
    assert 'totalBill' in list_display
    assert 'paymentPaid' in list_display

