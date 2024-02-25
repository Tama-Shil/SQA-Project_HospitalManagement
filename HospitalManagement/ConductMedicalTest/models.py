# models.py
from django.db import models

class TestRecord(models.Model):
    patient_id = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=255)
    patient_age = models.PositiveIntegerField(blank=True, null=True)
    referred_doctor = models.CharField(max_length=255)
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
    test_record_number = models.AutoField(primary_key=True)
    test_types = models.CharField(max_length=100, choices=TEST_TYPES)
    test_notes = models.TextField()

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if the object is being created (not updated)
            # Generate the test record number if it's a new record
            last_record = TestRecord.objects.order_by('-test_record_number').first()
            if last_record:
                self.test_record_number = last_record.test_record_number + 1
            else:
                self.test_record_number = 1
        super().save(*args, **kwargs)
