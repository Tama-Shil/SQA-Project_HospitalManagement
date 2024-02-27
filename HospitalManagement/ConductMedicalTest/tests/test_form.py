from django.test import TestCase
from forms import TestRecordForm

class TestRecordFormTests(TestCase):
    def test_valid_form(self):
        # Create a dictionary with valid form data
        form_data = {
            'patient_id': '123',
            'patient_name': 'John Doe',
            'patient_age': 30,
            'referred_doctor': 'Dr. Smith',
            'test_types': ['Blood Test ($50)', 'X-Ray ($100)'],
            'test_notes': 'Patient complained of chest pain.'
        }

        # Create a form instance with the valid data
        form = TestRecordForm(data=form_data)

        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Create a dictionary with invalid form data
        form_data = {
            'patient_id': '',  # Required field
            'patient_name': 'John Doe',
            'patient_age': 30,
            'referred_doctor': 'Dr. Smith',
            'test_types': [],  # At least one test type is required
            'test_notes': 'Patient complained of chest pain.'
        }

        # Create a form instance with the invalid data
        form = TestRecordForm(data=form_data)

        # Check if the form is invalid
        self.assertFalse(form.is_valid())
