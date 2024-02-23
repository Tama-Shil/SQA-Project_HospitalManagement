from django.test import TestCase, RequestFactory
from django.urls import reverse
from App_BuyMedicine.models import Patient
from App_BuyMedicine.forms import PatientIDForm
from App_BuyMedicine.views import checkPatient

class TestPatientViews(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_checkPatient_valid_post(self):
        # Create a test patient
        patient = Patient.objects.create(name='Test Patient', patientId='12345', gender='M', cabinNo='A101')

        # Prepare POST data with valid patient ID
        post_data = {'patient_id': '12345'}

        # Create a POST request
        request = self.factory.post(reverse('check_patient'), post_data)

        # Attach the session to the request
        request.session = {}

        # Call the view function
        response = checkPatient(request)

        # Check if the response is a redirect
        self.assertEqual(response.status_code, 302)  # Assuming you redirect upon success

    def test_checkPatient_invalid_post(self):
        # Prepare POST data with invalid patient ID
        post_data = {'patient_id': 'invalid_id'}

        # Create a POST request
        request = self.factory.post(reverse('check_patient'), post_data)

        # Attach the session to the request
        request.session = {}

        # Call the view function
        response = checkPatient(request)

        # Check if the response is not a redirect
        self.assertNotEqual(response.status_code, 302)  # Assuming you don't redirect upon failure
