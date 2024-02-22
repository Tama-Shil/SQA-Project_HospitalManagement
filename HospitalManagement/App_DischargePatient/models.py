
from django.db import models

class Patient(models.Model):
    """
    Model representing a patient in the hospital.

    :param name: The name of the patient.
    :type name: str
    :param patientId: The unique identifier of the patient.
    :type patientId: str
    :param gender: The gender of the patient. Choices are 'M' for Male, 'F' for Female, and 'O' for Other.
    :type gender: str
    :param cabinNo: The cabin number assigned to the patient.
    :type cabinNo: str
    :param totalBill: The total bill amount for the patient.
    :type totalBill: Decimal
    :param paymentPaid: A boolean indicating whether the payment has been made for the patient's bill.
    :type paymentPaid: bool
    """
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
