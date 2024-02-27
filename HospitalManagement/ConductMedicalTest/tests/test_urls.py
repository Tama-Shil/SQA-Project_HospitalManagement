from django.test import TestCase
from django.urls import reverse

class UrlTests(TestCase):
    def test_conduct_medical_test_url(self):
        # Test that the conductMedicalTest URL resolves to the correct view function
        url = reverse('conductMedicalTest')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Assuming the view returns HTTP 200 OK

    def test_another_url(self):
        # Test another URL in your application
        url = reverse('another_url_name')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Adjust the expected status code as needed

    # Add more test methods for other URLs in your application
