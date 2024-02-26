# make_appointment/tests/test_admin.py
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from make_appointment.models import Patient, Appointment

class AdminTestCase(TestCase):

    def setUp(self):
        # Create a superuser for accessing the admin site
        self.user = User.objects.create_superuser(username='admin', password='adminpass', email='admin@example.com')
        self.client = Client()
        self.client.force_login(self.user)

    def test_patient_model_is_registered(self):
        response = self.client.get(reverse('admin:make_appointment_patient_changelist'))
        self.assertEqual(response.status_code, 200)

    def test_appointment_model_is_registered(self):
        response = self.client.get(reverse('admin:make_appointment_appointment_changelist'))
        self.assertEqual(response.status_code, 200)
