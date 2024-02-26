from django.test import TestCase
from django.urls import reverse
from .forms import TestRecordForm

class UrlTests(TestCase):
    def test_conduct_medical_test_url(self):
        # Test that the conductMedicalTest URL resolves to the correct view function
        url = reverse('conductMedicalTest')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Assuming the view returns HTTP 200 OK

    # Add more tests for other URLs in your application


class ConductMedicalTestTestCase(TestCase):
    
    
    def test_form_submission_success(self):
        # Test submitting the form with valid data
        form_data = {
            'patient_id': '123',
            'patient_name': 'John Doe',
            'patient_age': 35,
            'referred_doctor': 'Dr. Smith',
            'test_types': ['Blood Test ($50)', 'X-Ray ($100)'],
            'test_notes': 'Some notes about the test',
        }
        response = self.client.post(reverse('conductMedicalTest'), form_data)
        self.assertEqual(response.status_code, 200)  # Assuming it redirects to a success page

    def test_form_submission_failure(self):
        # Test submitting the form with invalid data
        form_data = {
            # Missing patient name
            'patient_id': '123',
            'patient_age': 35,
            'referred_doctor': 'Dr. Smith',
            'test_types': ['Blood Test ($50)', 'X-Ray ($100)'],
            'test_notes': 'Some notes about the test',
        }
        response = self.client.post(reverse('conductMedicalTest'), form_data)
        self.assertEqual(response.status_code, 200)  # Should return to the same page with errors

    def test_generate_pdf(self):
        # Test generating a PDF with sample data
        data = [
            ['Field', 'Value'],
            ['Patient ID', '123'],
            ['Patient Name', 'John Doe'],
            ['Patient Age', 35],
            ['Referred Doctor', 'Dr. Smith'],
            ['Test Types', 'Blood Test ($50), X-Ray ($100)'],
            ['Notes', 'Some notes about the test'],
        ]
        pdf_response = generate_pdf(data)
        self.assertEqual(pdf_response.status_code, 200)
        # You can add more assertions to check the content or other aspects of the PDF response
