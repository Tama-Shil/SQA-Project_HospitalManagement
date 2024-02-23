# models.py

from django.db import models

class Patient(models.Model):
    """
    A model to represent a patient.

    Attributes:
        name (str): The name of the patient.
        patientId (str): The unique identifier of the patient.
        gender (str): The gender of the patient, chosen from predefined options.
        cabinNo (str): The cabin number of the patient.
    """
    name = models.CharField(max_length=100)
    patientId = models.CharField(max_length=10, primary_key=True,default='')  # Changed from IntegerField to CharField
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    cabinNo = models.CharField(max_length=10, default='')

class Medicine(models.Model):
    """
    A model to represent a medicine.

    Attributes:
        name (str): The name of the medicine.
        inStock (bool): Indicates whether the medicine is in stock or not.
        price (Decimal): The price of the medicine.
    """

    name = models.CharField(max_length=255)
    inStock = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        """
        Returns the name of the medicine.

        Returns:
            str: The name of the medicine.
        """
        return self.name
    