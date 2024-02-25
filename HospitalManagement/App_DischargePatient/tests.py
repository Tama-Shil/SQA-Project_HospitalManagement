from django.test import TestCase
from django.urls import reverse
from .models import Patient

class PatientTestCase(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(name='John Doe', patientId='123456', gender='M', cabinNo='C101', totalBill=100.00, paymentPaid=False)

    def test_patient_retrieval(self):
        retrieved_patient = Patient.objects.get(patientId='123456')
        self.assertEqual(retrieved_patient, self.patient)

