from django.test import TestCase
from .models import Prescription

class PrescriptionModelTest(TestCase):
    """
    Test cases for the Prescription model.
    """

    @classmethod
    def setUpTestData(cls):
        # Set up 5 data sets for testing
        Prescription.objects.create(
            patient_name='John Doe',
            age=30,
            gender='male',
            symptoms='Fever',
            diagnosis='Common cold',
            prescription='Rest and drink fluids',
            doctor_name='Dr. Smith',
            specialization='General Practitioner'
        )
        Prescription.objects.create(
            patient_name='Jane Smith',
            age=25,
            gender='female',
            symptoms='Headache',
            diagnosis='Migraine',
            prescription='Take painkillers and rest',
            doctor_name='Dr. Johnson',
            specialization='Neurologist'
        )
        Prescription.objects.create(
            patient_name='Michael Brown',
            age=40,
            gender='male',
            symptoms='Sore throat',
            diagnosis='Strep throat',
            prescription='Antibiotics and plenty of fluids',
            doctor_name='Dr. White',
            specialization='ENT Specialist'
        )
        Prescription.objects.create(
            patient_name='Emily Davis',
            age=35,
            gender='female',
            symptoms='Cough',
            diagnosis='Bronchitis',
            prescription='Cough syrup and steam inhalation',
            doctor_name='Dr. Lee',
            specialization='Pulmonologist'
        )
        Prescription.objects.create(
            patient_name='David Johnson',
            age=50,
            gender='male',
            symptoms='Fatigue',
            diagnosis='Anemia',
            prescription='Iron supplements and dietary changes',
            doctor_name='Dr. Green',
            specialization='Hematologist'
        )

    def test_prescription_count(self):
        # Check if the total number of prescriptions is 5
        self.assertEqual(Prescription.objects.count(), 5)

    def test_prescription_patient_name(self):
        # Check patient names for each data set
        prescription_names = [prescription.patient_name for prescription in Prescription.objects.all()]
        expected_names = ['John Doe', 'Jane Smith', 'Michael Brown', 'Emily Davis', 'David Johnson']
        self.assertEqual(prescription_names, expected_names)

    def test_prescription_age_average(self):
        # Check the average age of patients
        average_age = sum([prescription.age for prescription in Prescription.objects.all()]) / 5
        self.assertAlmostEqual(average_age, 36, places=2)

    def test_prescription_diagnosis_contains(self):
        # Check if 'throat' is in any diagnosis
        diagnoses = [prescription.diagnosis for prescription in Prescription.objects.all()]
        self.assertTrue(any('throat' in diagnosis for diagnosis in diagnoses))

    def test_prescription_male_doctors(self):
        # Check if there are any male doctors
        male_doctors_count = Prescription.objects.filter(gender='male').count()
        self.assertNotEqual(male_doctors_count, 0)

    def test_prescription_specialization_unique(self):
        # Check if all specializations are unique
        specializations = set([prescription.specialization for prescription in Prescription.objects.all()])
        self.assertEqual(len(specializations), 5)

    def test_prescription_doctor_name_not_blank(self):
        # Check if doctor names are not blank
        doctor_names = [prescription.doctor_name for prescription in Prescription.objects.all()]
        self.assertTrue(all(doctor_names))
