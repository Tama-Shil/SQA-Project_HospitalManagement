
from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)   
    patientId = models.CharField(max_length=10, primary_key=True)  # Changed from IntegerField to CharField
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    cabinNo = models.CharField(max_length=10)
    totalBill = models.DecimalField(max_digits=10, decimal_places=2)
    paymentPaid = models.BooleanField(default=False)
