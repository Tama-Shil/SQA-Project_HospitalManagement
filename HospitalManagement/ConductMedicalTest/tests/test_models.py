from django.test import TestCase
from models import TestRecord

class TestRecordModelTests(TestCase):
    def test_create_test_record(self):
        # Create a test record
        TestRecord.objects.create(
            patient_id="123",
            patient_name="John Doe",
            patient_age=30,
            referred_doctor="Dr. Smith",
            test_types="Blood Test ($50), X-Ray ($100)",
            test_notes="Patient complained of chest pain."
        )

        # Retrieve the test record from the database
        test_record = TestRecord.objects.get(patient_id="123")

        # Check if the test record was created correctly
        self.assertEqual(test_record.patient_name, "John Doe")
        self.assertEqual(test_record.patient_age, 30)
        self.assertEqual(test_record.referred_doctor, "Dr. Smith")
        self.assertEqual(test_record.test_types, "Blood Test ($50), X-Ray ($100)")
        self.assertEqual(test_record.test_notes, "Patient complained of chest pain.")
