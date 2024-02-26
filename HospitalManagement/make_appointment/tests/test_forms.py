# make_appointment/tests/test_forms.py
from django.test import TestCase
from make_appointment.models import Patient, Appointment
from make_appointment.forms import AppointmentForm
from datetime import date, time

class AppointmentFormTest(TestCase):

    def test_appointment_form_valid_data(self):
        patient = Patient.objects.create(name="John Doe", contact_number="123456789")
        form_data = {
            'patient': patient.id,
            'date': '2024-02-26',
            'time': '14:30',
        }
        form = AppointmentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_appointment_form_invalid_data(self):
        form_data = {
            'patient': '',  # Empty patient field to make the form invalid
            'date': '2022-01-01',
            'time': '10:00',
        }
        form = AppointmentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('patient', form.errors)
        self.assertEqual(form.errors['patient'][0], 'This field is required.')

    # Add more test cases as needed
