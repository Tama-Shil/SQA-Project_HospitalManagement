from django.db import models

class Hospital_User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # You may want to use a more secure field such as PasswordField
    address = models.CharField(max_length=255)
    cell_number = models.CharField(max_length=15)
    TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )
    user_type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return self.username
