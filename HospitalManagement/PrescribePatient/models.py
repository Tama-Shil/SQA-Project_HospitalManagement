"""
Module: prescribe_patient

This module contains a Django model for representing a prescription.

"""
from django.db import models

class Prescription(models.Model):
    """
    Model representing a prescription.
    """
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField(help_text="Enter patient's age")
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    symptoms = models.TextField(help_text="Enter patient's symptoms")
    diagnosis = models.TextField(help_text="Enter diagnosis")
    prescription = models.TextField(help_text="Enter prescription details")
    doctor_name = models.CharField(max_length=100, help_text="Enter doctor's name")
    specialization = models.CharField(max_length=100, help_text="Enter doctor's specialization")

    def __str__(self):
        """
        String for representing the Prescription object.
        """
        return f"Prescription for {self.patient_name} by Dr. {self.doctor_name}"
