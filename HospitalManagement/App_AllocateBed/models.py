from django.db import models

# Create your models here.
class Bed(models.Model):
    BED_TYPES = (
        ('general', 'General'),
        ('private', 'Private'),
        ('intensive_care', 'Intensive Care'),
    )
    
    bedNumber = models.CharField(max_length=20)
    bedType = models.CharField(max_length=20, choices=BED_TYPES)
    isOccupied = models.BooleanField(default=False)
    
    def __str__(self):
        return self.bedNumber
    

class Patient(models.Model):
    GENDER_TYPES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_TYPES)
    assignedBed = models.ForeignKey(Bed, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, default='Admitted')

    def __str__(self):
        return self.firstName + " " + self.lastName