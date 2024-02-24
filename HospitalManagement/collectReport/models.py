# collectReport/models.py
from django.db import models

class Patient(models.Model):
    patient_id = models.CharField(max_length=10)
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    blood_test = models.BooleanField(default=False)
    x_ray = models.BooleanField(default=False)
    urine_analysis = models.BooleanField(default=False)

    def __str__(self):
        return self.patient_name
