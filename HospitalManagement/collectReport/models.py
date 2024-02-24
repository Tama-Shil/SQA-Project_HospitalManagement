# collectReport/models.py
from django.db import models

class Patient(models.Model):
    """
    Model representing a patient and their medical information.

    Attributes:
    - patient_id (CharField): The unique identifier for the patient.
    - patient_name (CharField): The name of the patient.
    - age (IntegerField): The age of the patient.
    - gender (CharField): The gender of the patient.
    - blood_test (BooleanField): Indicates if a blood test has been conducted for the patient.
    - x_ray (BooleanField): Indicates if an X-ray has been conducted for the patient.
    - urine_analysis (BooleanField): Indicates if a urine analysis has been conducted for the patient.
    """

    patient_id = models.CharField(max_length=10)
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    blood_test = models.BooleanField(default=False)
    x_ray = models.BooleanField(default=False)
    urine_analysis = models.BooleanField(default=False)

    def __str__(self):
        """
        String representation of the patient.

        Returns:
        - str: The patient's name.
        """
        return self.patient_name
