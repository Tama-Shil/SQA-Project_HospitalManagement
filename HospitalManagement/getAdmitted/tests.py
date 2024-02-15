# tests.py

from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Patient

class PatientModelTestCase(TestCase):
    def testValidPatientCreation(self):
        """
        Test creating a valid Patient model instance.

        Ensures that a Patient instance can be created with valid data.
        """
        valid_patient_data = {
            'name': 'Hasan',
            'age': 25,
            'gender': 'male',
            'admissionDate': '2024-01-01',
            'contact': '12345678901',
            'address': 'Chittagong',
            'symptoms': 'Fever, cough',
        }
        patient = Patient.objects.create(**valid_patient_data)
        self.assertEqual(patient.name, 'Hasan')

    def testInvalidContactNumber(self):
        """
        Test creating a Patient model instance with an invalid contact number.

        Ensures that a ValidationError is raised when an invalid contact number is provided.
        """
        invalid_patient_data = {
            'name': 'Khadija',
            'age': 30,
            'gender': 'female',
            'admissionDate': '2024-02-15',
            'contact': '12345',  # Invalid: less than 11 digits
            'address': 'Khulna',
            'symptoms': 'Headache',
        }

        patient = Patient(**invalid_patient_data)

        try:
            patient.full_clean()  # Trigger validation
        except ValidationError as e:
            print("ValidationError caught:", e)
            return

        self.fail("ValidationError not raised")

    def testInvalidMissingName(self):
        """
        Test creating a Patient model instance with a missing 'name' field.

        Ensures that a ValidationError is raised when the required 'name' field is missing.
        """
        invalid_patient_data = {
            'age': 40,
            'gender': 'male',
            'admissionDate': '2024-03-01',
            'contact': '98765432109',
            'address': 'Dhaka',
            'symptoms': 'Fatigue',
        }

        patient = Patient(**invalid_patient_data)

        try:
            patient.full_clean()  # Trigger validation
        except ValidationError as e:
            print("ValidationError caught:", e)
            return

        self.fail("ValidationError not raised")
