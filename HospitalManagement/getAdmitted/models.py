from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Patient(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    name = models.CharField(max_length = 64)
    age = models.IntegerField()
    gender = models.CharField(max_length = 10, choices = GENDER_CHOICES)
    admissionDate = models.DateField()
    contact = models.CharField(max_length = 11)
    address = models.TextField()
    symptoms = models.TextField()


    def __str__(self):
        return self.name

