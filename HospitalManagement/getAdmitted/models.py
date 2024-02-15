# models.py

from django.db import models
from django.core.validators import RegexValidator

class Patient(models.Model):
    """
    Model representing a patient in the hospital.

    This model defines the fields for storing information about a patient,
    including their name, age, gender, admission date, contact information,
    address, and symptoms.
    """

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    """
    Choices for the gender field in the Patient model.

    The choices are a list of tuples where the first element in each tuple
    is the actual value to be stored in the database, and the second element
    is the human-readable name for the option.
    """

    name = models.CharField(max_length=64)
    """
    CharField representing the name of the patient.

    The maximum length is set to 64 characters.
    """

    age = models.IntegerField()
    """
    IntegerField representing the age of the patient.
    """

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    """
    CharField representing the gender of the patient.

    Choices are restricted to the options specified in GENDER_CHOICES.
    """

    admissionDate = models.DateField()
    """
    DateField representing the admission date of the patient.
    """

    contact = models.CharField(
        max_length=11,
        validators=[RegexValidator(regex=r'^\d{11}$', message='Enter a valid 11-digit phone number.')]
    )
    """
    CharField representing the contact number of the patient.

    The field is validated using a RegexValidator to ensure it's an 11-digit phone number.
    """

    address = models.TextField()
    """
    TextField representing the address of the patient.
    """

    symptoms = models.TextField()
    """
    TextField representing the symptoms reported by the patient.
    """

    def __str__(self):
        """
        String representation of the Patient object.

        Returns the name of the patient as the string representation.
        """
        return self.name
