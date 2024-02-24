# collectReport/tests/test_forms.py
from django.test import TestCase
from collectReport.forms import Report
from collectReport.models import Patient

class ReportFormTest(TestCase):
    """
    Test suite for the Report form in the collectReport app.
    """

    def setUp(self):
        """
        Set up any necessary data or resources for the test cases.
        """
        pass

    def testReportFormValidData(self):
        """
        Test the Report form with valid data.
        """
        valid_data = {
            'patient_id': 'P001',
            'patient_name': 'John Doe',
            'age': 30,
            'gender': 'Male',
            'blood_test': True,
            'x_ray': False,
            'urine_analysis': True
        }
        form = Report(data=valid_data)
        self.assertTrue(form.is_valid())

    def testReportFormBlankData(self):
        """
        Test the Report form with blank data, expecting it to be invalid.
        """
        blank_data = {}
        form = Report(data=blank_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 7)  # Expecting errors for all fields

    def testReportFormInvalidAge(self):
        """
        Test the Report form with invalid age (e.g., negative value), expecting it to be invalid.
        """
        invalid_data = {
            'patient_id': 'P001',
            'patient_name': 'John Doe',
            'age': -5,
            'gender': 'Male',
            'blood_test': True,
            'x_ray': False,
            'urine_analysis': True
        }
        form = Report(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('age', form.errors)  # Expecting an error for the 'age' field
