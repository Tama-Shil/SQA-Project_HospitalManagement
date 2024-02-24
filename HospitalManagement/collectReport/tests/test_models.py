# collectReport/tests/test_models.py
from django.test import TestCase
from collectReport.models import Patient

class PatientModelTest(TestCase):
    """
    Test suite for the Patient model in the collectReport app.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        Patient.objects.create(
            patient_id='P001',
            patient_name='John Doe',
            age=30,
            gender='Male',
            blood_test=True,
            x_ray=False,
            urine_analysis=True
        )

    def testPatientName(self):
        """
        Test the retrieval of the patient name from the Patient model.
        """
        patient = Patient.objects.get(id=1)
        expected_name = f'{patient.patient_name}'
        self.assertEqual(expected_name, 'John Doe')

    def testPatientAge(self):
        """
        Test the retrieval of the patient age from the Patient model.
        """
        patient = Patient.objects.get(id=1)
        expected_age = patient.age
        self.assertEqual(expected_age, 30)

    def testPatientGender(self):
        """
        Test the retrieval of the patient gender from the Patient model.
        """
        patient = Patient.objects.get(id=1)
        expected_gender = f'{patient.gender}'
        self.assertEqual(expected_gender, 'Male')

    def testBloodTestDefaultValue(self):
        """
        Test the default value of the blood_test field in the Patient model.
        """
        patient = Patient.objects.get(id=1)
        expected_value = patient.blood_test
        self.assertEqual(expected_value, True)

    def testXRayDefaultValue(self):
        """
        Test the default value of the x_ray field in the Patient model.
        """
        patient = Patient.objects.get(id=1)
        expected_value = patient.x_ray
        self.assertEqual(expected_value, False)

    def testUrineAnalysisDefaultValue(self):
        """
        Test the default value of the urine_analysis field in the Patient model.
        """
        patient = Patient.objects.get(id=1)
        expected_value = patient.urine_analysis
        self.assertEqual(expected_value, True)
