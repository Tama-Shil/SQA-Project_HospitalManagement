"""
Module: models

Description:
This module defines the database models for the medical test management app.
It contains the TestRecord model, which represents a record of medical tests conducted.

Model:
    - TestRecord: Represents a record of medical tests conducted, including patient information,
                  test types, and test notes. It also generates a unique test record number
                  for each new record.

Attributes:
    - patientId (CharField): Identifier for the patient, limited to 100 characters.
    - patientName (CharField): Name of the patient, limited to 255 characters.
    - patientAge (PositiveIntegerField): Age of the patient (optional).
    - referredDoctor (CharField): Name of the doctor who referred the patient, limited to 255 characters.
    - testRecordNumber (AutoField): Primary key representing the unique test record number.
    - testTypes (CharField): Choices field representing the types of tests conducted.
    - testNotes (TextField): Additional notes or comments regarding the test.

Methods:
    - save(): Overrides the save method to generate a unique test record number
              when a new record is created.

"""

from django.db import models

class TestRecord(models.Model):
    patientId = models.CharField(max_length=100)
    patientName = models.CharField(max_length=255)
    patientAge = models.PositiveIntegerField(blank=True, null=True)
    referredDoctor = models.CharField(max_length=255)
    TEST_TYPES = [
        ('Blood Test ($50)', 'Blood Test ($50)'),
        ('Urinalysis ($40)', 'Urinalysis ($40)'),
        ('X-Ray ($100)', 'X-Ray ($100)'),
        ('MRI ($200)', 'MRI ($200)'),
        ('CT Scan ($150)', 'CT Scan ($150)'),
        ('Ultrasound ($80)', 'Ultrasound ($80)'),
        ('ECG ($60)', 'ECG ($60)'),
        ('Endoscopy ($180)', 'Endoscopy ($180)'),
        ('Colonoscopy ($200)', 'Colonoscopy ($200)'),
        ('Biopsy ($120)', 'Biopsy ($120)'),
        # Add more test types here if needed
    ]
    testRecordNumber = models.AutoField(primary_key=True)
    testTypes = models.CharField(max_length=100, choices=TEST_TYPES)
    testNotes = models.TextField()

    def save(self, *args, **kwargs):
        """
        Overrides the save method to generate a unique test record number
        when a new record is created.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        if not self.pk:  # Check if the object is being created (not updated)
            # Generate the test record number if it's a new record
            lastRecord = TestRecord.objects.order_by('-testRecordNumber').first()
            if lastRecord:
                self.testRecordNumber = lastRecord.testRecordNumber + 1
            else:
                self.testRecordNumber = 1
        super().save(*args, **kwargs)
