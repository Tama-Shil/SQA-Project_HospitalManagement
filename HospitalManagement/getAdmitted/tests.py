from django.test import TestCase
from django.urls import reverse
from .models import Patient

class PatientAdmissionTest(TestCase):
    def test_patient_admission(self):
        # Create a patient data dictionary
        patient_data = {
            'name': 'Hasan',
            'age': 30,
            'gender': 'male',
            'admissionDate': '2022-01-01',
            'contact': '1234567890',
            'address': '123 Main St, City',
            'symptoms': 'Fever, cough',
        }

        # Perform the patient admission by sending a POST request
        response = self.client.post(reverse('savePatientData'), patient_data)

        # Check if the patient is added successfully
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Patient.objects.filter(name='John Doe').exists())

