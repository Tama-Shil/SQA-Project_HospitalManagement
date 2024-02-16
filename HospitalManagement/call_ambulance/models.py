# call_ambulance/models.py

from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    # Add other fields as needed

class Patient(models.Model):
    name = models.CharField(max_length=255)
    # Add other fields as needed

class AmbulanceCall(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add other fields as needed

