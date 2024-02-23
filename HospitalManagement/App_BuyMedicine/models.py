# models.py

from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    patientId = models.CharField(max_length=10, primary_key=True,default='')  # Changed from IntegerField to CharField
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    cabinNo = models.CharField(max_length=10, default='')

