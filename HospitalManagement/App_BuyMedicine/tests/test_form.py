import pytest
from App_BuyMedicine.forms import PatientIDForm

@pytest.mark.django_db
class TestPatientIDForm:
    
    def test_patient_id_form_valid(self):
        form_data = {'patient_id': '1234567890'}
        form = PatientIDForm(data=form_data)
        assert form.is_valid() == True
    

    def test_patient_id_form_invalid_long_id(self):
        form_data = {'patient_id': '12345678901'}
        form = PatientIDForm(data=form_data)
        assert form.is_valid() == False
    
    def test_patient_id_form_invalid_empty_id(self):
        form_data = {}
        form = PatientIDForm(data=form_data)
        assert form.is_valid() == False
