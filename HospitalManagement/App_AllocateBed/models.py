from django.db import models

# Create your models here.
class Bed(models.Model):
    BED_TYPES = (
        ('general', 'General'),
        ('private', 'Private'),
        ('intensive_care', 'Intensive Care'),
    )
    
    bed_number = models.CharField(max_length=20)
    bed_type = models.CharField(max_length=20, choices=BED_TYPES)
    is_occupied = models.BooleanField(default=False)
    
    def __str__(self):
        return self.bed_number
    

class Patient(models.Model):
    GENDER_TYPES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_TYPES)
    assigned_bed = models.ForeignKey(Bed, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, default='Admitted')

    def __str__(self):
        return self.first_name + " " + self.last_name