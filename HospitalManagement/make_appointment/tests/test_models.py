# make_appointment/tests/test_models.py
from django.test import TestCase
from make_appointment.models import Patient, Appointment
from datetime import date, time

class PatientModelTest(TestCase):

    def test_patient_str_method(self):
        patient = Patient(name="John Doe", contact_number="123456789")
        self.assertEqual(str(patient), "John Doe")

class AppointmentModelTest(TestCase):

    def test_appointment_str_method(self):
        patient = Patient(name="John Doe", contact_number="123456789")
        appointment = Appointment(patient=patient, date=date(2024, 2, 26), time=time(14, 30))
        expected_str = "John Doe's Appointment on 2024-02-26 at 14:30:00"
        self.assertEqual(str(appointment), expected_str)
