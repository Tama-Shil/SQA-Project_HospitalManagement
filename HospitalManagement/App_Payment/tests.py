from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError
from .models import Patient
from .views import selectPaymentMethod

class PaymentMethodViewTestCase(TestCase):
    """
    Test case for the payment method views.

    :Tests:
        1. Test the GET request for selecting a payment method.
        2. Test the POST request for selecting a payment method with an existing patient.
        3. Test the POST request for selecting a payment method with a new patient.
    """

    def test_get_request(self):
        """
        Test the GET request for selecting a payment method.

        :return: None
        """
        url = reverse('select_payment_method')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'selectPaymentMethod.html')

    def test_post_request_existing_patient(self):
        """
        Test the POST request for selecting a payment method with an existing patient.

        :return: None
        """
        
        patient = Patient.objects.create(patient_id='P001', patient_name='John Doe', cabin_number='C101')
        data = {'patient_id': 'P001', 'patient_name': 'John Doe'}
        url = reverse('select_payment_method')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'payment_success.html')

    def test_post_request_new_patient(self):
        """
        Test the POST request for selecting a payment method with a new patient.
        
        :return: None
        """
        data = {'patient_id': 'P002', 'patient_name': 'Jane Smith'}
        url = reverse('select_payment_method')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'payment_success.html')

class PatientModelTestCase(TestCase):
    """
    Test case for the Patient model.

    :Tests:
        1. Test creating a valid Patient model instance.
        2. Test creating an invalid Patient model instance.
    """

    def test_valid_patient_creation(self):
        """
        Test creating a valid Patient model instance.

        :return: None
        """
        valid_patient_data = {
            'patient_id': 'P001',
            'patient_name': 'John Doe',
            'cabin_number': 'C101',
        }
        patient = Patient.objects.create(**valid_patient_data)
        self.assertEqual(patient.patient_name, 'John Doe')

    def test_invalid_patient_creation(self):
        """
        Test creating an invalid Patient model instance.

        :return: None
        """
        # Missing patient_id which is required
        invalid_patient_data = {
            'patient_name': 'Jane Smith',
            'cabin_number': 'C102',
        }
        with self.assertRaises(ValidationError):
            patient = Patient(**invalid_patient_data)
            patient.full_clean()
