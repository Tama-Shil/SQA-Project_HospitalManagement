"""
Django Models
-------------

This module defines Django models for App_Payment.
"""

from django.db import models

class Patient(models.Model):
    """
    Model representing a patient in the hospital.

    :param patient_id: The unique ID of the patient.
    :type patient_id: str, max length 20
    :param patient_name: The name of the patient.
    :type patient_name: str, max length 100
    :param cabin_number: The number of the cabin assigned to the patient.
    :type cabin_number: str, max length 100
    :param reports_bill: The bill for reports associated with the patient.
    :type reports_bill: Decimal, max digits 10, decimal places 2, default 0
    :param medicine_bill: The bill for medicines associated with the patient.
    :type medicine_bill: Decimal, max digits 10, decimal places 2, default 0
    :param cabin_bill: The bill for the cabin assigned to the patient.
    :type cabin_bill: Decimal, max digits 10, decimal places 2, default 0
    :param total_bill: The total bill amount for the patient.
    :type total_bill: Decimal, max digits 10, decimal places 2, default 0

    :return: String representation of the patient model instance.
    :rtype: str
    """

    patient_id = models.CharField(max_length=20)
    patient_name = models.CharField(max_length=100)
    cabin_number = models.CharField(max_length=100)
    reports_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    medicine_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cabin_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        """
            method to return the patient's name as its string representation.

        """

        return self.patient_name
