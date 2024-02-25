import pytest
from App_DischargePatient.models import Patient
from App_DischargePatient.forms import DischargeForm

@pytest.mark.django_db
def test_discharge_form_valid():
    # Create a valid patient ID
    patient_id = 'P001'

    # Create a form instance with valid data
    form = DischargeForm(data={'patientId': patient_id})

    # Assert that the form is valid
    assert form.is_valid()

@pytest.mark.django_db
def test_discharge_form_invalid():
    # Create an invalid patient ID (empty string)
    patient_id = ''

    # Create a form instance with invalid data
    form = DischargeForm(data={'patientId': patient_id})

    # Assert that the form is not valid
    assert not form.is_valid()
