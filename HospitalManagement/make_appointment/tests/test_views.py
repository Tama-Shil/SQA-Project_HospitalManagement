# make_appointment/tests/test_views.py
from django.test import TestCase, RequestFactory
from django.urls import reverse
from make_appointment.models import Patient, Appointment
from make_appointment.views import make_appointment, appointment_success
from make_appointment.forms import AppointmentForm
from datetime import date, time

class MakeAppointmentViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_make_appointment_view_GET(self):
        response = self.client.get(reverse('make_appointment'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'make_appointment/make_appointment.html')
        self.assertIsInstance(response.context['form'], AppointmentForm)

    def test_make_appointment_view_POST_valid_data(self):
        patient = Patient.objects.create(name="John Doe", contact_number="123456789")
        form_data = {
            'patient': patient.id,
            'date': '2024-02-26',
            'time': '14:30',
        }
        response = self.client.post(reverse('make_appointment'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertEqual(Appointment.objects.count(), 1)

    def test_make_appointment_view_POST_invalid_data(self):
        form_data = {
            'patient': '',  # Empty patient field to make the form invalid
            'date': '2022-01-01',
            'time': '10:00',
        }
        response = self.client.post(reverse('make_appointment'), data=form_data)
        self.assertEqual(response.status_code, 200)  # Form submission failed, stay on the same page
        self.assertFalse(Appointment.objects.exists())

class AppointmentSuccessViewTest(TestCase):

    def test_appointment_success_view(self):
        response = self.client.get(reverse('appointment_success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'make_appointment/appointment_success.html')
