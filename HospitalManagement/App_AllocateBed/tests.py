from django.test import TestCase
from django.urls import reverse
from .models import Bed, Patient
from .forms import BedForm, PatientForm

class BedModelTestCase(TestCase):
    """
    Test cases for the Bed model.
    """
    def setUp(self):
        self.bed = Bed.objects.create(bedNumber='101', bedType='general')

    def test_bed_str_representation(self):
        """
        Test the string representation of the Bed model.
        """
        self.assertEqual(str(self.bed), '101')

class PatientModelTestCase(TestCase):
    """
    Test cases for the Patient model.
    """
    def setUp(self):
        self.bed = Bed.objects.create(bedNumber='101', bedType='general')
        self.patient = Patient.objects.create(firstName='Alen', lastName='Mux', age=30, gender='male', assignedBed=self.bed)

    def test_patient_str_representation(self):
        """
        Test the string representation of the Patient model.
        """
        self.assertEqual(str(self.patient), 'Alen Mux')

class HomeViewTestCase(TestCase):
    """
    Test cases for the home view.
    """
    def test_home_view(self):
        """
        Test the home view.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

class AddBedViewTestCase(TestCase):
    """
    Test cases for the add bed view.
    """
    def test_add_bed_view_get(self):
        """
        Test the GET request to the add bed view.
        """
        response = self.client.get(reverse('add_bed'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_bed.html')

    def test_add_bed_view_post(self):
        """
        Test the POST request to the add bed view.
        """
        data = {'bedNumber': '102', 'bedType': 'private'}
        response = self.client.post(reverse('add_bed'), data)
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Bed.objects.count(), 1)    

class AddPatientViewTestCase(TestCase):
    """
    Test cases for the add patient view.
    """
    def test_add_patient_view_get(self):
        """
        Test the GET request to the add patient view.
        """
        response = self.client.get(reverse('add_patient'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_patient.html')

    def test_add_patient_view_post_invalid_data(self):
        """
        Test the POST request to the add patient view with invalid data.
        """
        data = {'firstName': 'Jane', 'lastName': 'Doe', 'age': 'twenty-five', 'gender': 'female'}  
        """
        Invalid age
        """
        response = self.client.post(reverse('add_patient'), data)
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(Patient.objects.count(), 0) 
