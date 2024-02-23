# collectReport/tests/test_models.py
from django.test import TestCase
from collectReport.models import PatientReport , MedicalTest


class PatientReportModelTest(TestCase):
    def testCreatePatientReport(self):
        patient = PatientReport.objects.create(
            patient_id="123",
            patient_name="John Doe",
            age=30,
            gender="male"
        )
        self.assertEqual(patient.patient_id, "123")
        self.assertEqual(patient.patient_name, "John Doe")
        self.assertEqual(patient.age, 30)
        self.assertEqual(patient.gender, "male")

    def testPatientReportHasTests(self):
        blood_test = MedicalTest.objects.create(name="Blood Test")
        urine_analysis = MedicalTest.objects.create(name="Urine Analysis")

        patient = PatientReport.objects.create(
            patient_id="456",
            patient_name="Jane Doe",
            age=25,
            gender="female"
        )

        patient.tests.add(blood_test)
        patient.tests.add(urine_analysis)

        self.assertEqual(patient.tests.count(), 2)
        self.assertIn(blood_test, patient.tests.all())
        self.assertIn(urine_analysis, patient.tests.all())

class MedicalTestModelTest(TestCase):
    def testCreateMedicalTest(self):
        test = MedicalTest.objects.create(name="X-ray")
        self.assertEqual(test.name, "X-ray")
