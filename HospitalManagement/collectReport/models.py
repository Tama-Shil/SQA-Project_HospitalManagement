# collectReport/models.py
from django.db import models

class PatientReport(models.Model):
    patient_id = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    tests = models.ManyToManyField('MedicalTest')

class MedicalTest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
