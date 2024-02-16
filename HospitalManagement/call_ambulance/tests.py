from django.test import TestCase, Client 
from .models import Hospital, Patient, AmbulanceCall
from datetime import datetime
from django.urls import reverse

class HospitalModelTest(TestCase):
    """
    Test cases for the Hospital model.
    """
    def test_str_representation(self): 
        """
        Test the string representation of the Hospital model.
        """
        hospital = Hospital(name='Test Hospital')
        self.assertEqual(str(hospital), 'Test Hospital')

class PatientModelTest(TestCase):
    """
    Test cases for the Patient model
    """
    def test_str_representation(self):
        """
        Test the string representation of the Patient model.
        """
        patient = Patient(name='Test Patient')
        self.assertEqual(str(patient), 'Test Patient')

class AmbulanceCallModelTest(TestCase):
    """
    Test cases for the AmbulanceCall model.
    """
    def test_str_representation(self):
        """
        Test the string representation of the AmbulanceCall model.
        """
        hospital = Hospital.objects.create(name='Test Hospital')
        patient = Patient.objects.create(name='Test Patient')
        ambulance_call = AmbulanceCall.objects.create(
            patient=patient,
            hospital=hospital,
            timestamp=datetime.now(),
        )
        expected_str = f"Ambulance call for {patient} to {hospital} at {ambulance_call.timestamp}"
        self.assertEqual(str(ambulance_call), expected_str)


class AmbulanceCallFormViewTest(TestCase):
    """
    Test cases for the AmbulanceCallFormView.
    """
    def setUp(self):
        self.client = Client()

    def test_ambulance_call_form_view(self):
        """
        Test the AmbulanceCallFormView by checking the rendered template.
        """
        response = self.client.get(reverse('call_ambulance:call_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'call_ambulance/call_ambulance_form.html')

    def test_ambulance_dispatch_view_successful(self):
        """
        Test the AmbulanceDispatchView with successful form submission.
        """
        hospital = Hospital.objects.create(name='Test Hospital')
        patient = Patient.objects.create(name='Test Patient')
        data ={
            'patient_name': 'Test Patient',
            'hospital': hospital.id,
            'phone_number': '1234567890',
        }
        response = self.client.post(reverse('call_ambulance:dispatch'), data)
        self.assertRedirects(response, reverse('call_ambulance:dispatch_success'))
        self.assertEqual(AmbulanceCall.objects.count(), 1)

    def test_ambulance_dispatch_view_failure(self):
        """
        Test the AmbulanceDispatchView with a failed form submission.

        returns: None
        """
        # Test with incomplete data to trigger an exception
        data = {
            'patient_name': 'Test Patient',
            'phone_number': '1234567890',
        }
        response = self.client.post(reverse('call_ambulance:dispatch'), data)
        self.assertRedirects(response, reverse('call_ambulance:call_form'))
        self.assertEqual(AmbulanceCall.objects.count(), 0)
