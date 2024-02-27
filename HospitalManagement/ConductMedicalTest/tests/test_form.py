"""
Module: test_forms

Description:
This module contains test cases for the forms used in the ConductMedicalTest app.

Classes:
    - TestRecordFormTests: Test cases for the TestRecordForm form.
"""

from django.test import TestCase
from ..forms import TestRecordForm

class TestRecordFormTests(TestCase):
    """
    Test cases for the TestRecordForm form.
    """
    def test_valid_form(self):
        """
        Test if the form is valid with valid data.
        """
        # Create a dictionary with valid form data
        formData = {
            'patientId': '123',
            'patientName': 'John Doe',
            'patientAge': 30,
            'referredDoctor': 'Dr. Smith',
            'testTypes': ['Blood Test ($50)', 'X-Ray ($100)'],
            'testNotes': 'Patient complained of chest pain.'
        }

        # Create a form instance with the valid data
        form = TestRecordForm(data=formData)

        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """
        Test if the form is invalid with invalid data.
        """
        # Create a dictionary with invalid form data
        formData = {
            'patientId': '',  # Required field
            'patientName': 'John Doe',
            'patientAge': 30,
            'referredDoctor': 'Dr. Smith',
            'testTypes': [],  # At least one test type is required
            'testNotes': 'Patient complained of chest pain.'
        }

        # Create a form instance with the invalid data
        form = TestRecordForm(data=formData)

        # Check if the form is invalid
        self.assertFalse(form.is_valid())
