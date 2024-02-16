# call_ambulance/models.py
"""
Django Models
-------------

This module defines Django models for call_ambulance.
"""

from django.db import models

class Hospital(models.Model):
    """
    Represents a hospital in the system.

    Attributes:
        name (str): The name of the hospital.
        # Add other fields as needed
    """
    name = models.CharField(max_length=255)
    # Add other fields as needed

    def __str__(self):
        """
        Return a human-readable string representation of the hospital.
        """
        return self.name

class Patient(models.Model):
    """
    Represents a patient in the system.

    Attributes:
        name (str): The name of the patient.
        # Add other fields as needed
    """
    name = models.CharField(max_length=255)
    # Add other fields as needed

    def __str__(self):
        """
        Return a human-readable string representation of the patient.
        """
        return self.name

class AmbulanceCall(models.Model):
    """
    Represents an ambulance call in the system.

    Attributes:
        patient (Patient): The patient who needs an ambulance.
        hospital (Hospital): The hospital the ambulance is dispatched to.
        timestamp (datetime): The timestamp of the ambulance call.
        # Add other fields as needed
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add other fields as needed

    def __str__(self):
        """
        Return a human-readable string representation of the ambulance call.
        """
        return f"Ambulance call for {self.patient} to {self.hospital} at {self.timestamp}"
