"""
Module: TestRecordModelTests

Description:
This module contains unit tests for the TestRecord model.

Functions:
    - testCreateTestRecord: Tests the creation of a test record in the database.
"""
from django.test import TestCase
from models import TestRecord

class TestRecordModelTests(TestCase):
    """
    Module: TestRecordModelTests

    Description:
    This module contains unit tests for the TestRecord model.

    Functions:
        - testCreateTestRecord: Tests the creation of a test record in the database.
    """
    def testCreateTestRecord(self):
        """
        Test if a test record can be created successfully.
        """
        # Create a test record
        TestRecord.objects.create(
            patientId="123",
            patientName="John Doe",
            patientAge=30,
            referredDoctor="Dr. Smith",
            testTypes="Blood Test ($50), X-Ray ($100)",
            testNotes="Patient complained of chest pain."
        )

        # Retrieve the test record from the database
        testRecord = TestRecord.objects.get(patientId="123")

        # Check if the test record was created correctly
        self.assertEqual(testRecord.patientName, "John Doe")
        self.assertEqual(testRecord.patientAge, 30)
        self.assertEqual(testRecord.referredDoctor, "Dr. Smith")
        self.assertEqual(testRecord.testTypes, "Blood Test ($50), X-Ray ($100)")
        self.assertEqual(testRecord.testNotes, "Patient complained of chest pain.")
