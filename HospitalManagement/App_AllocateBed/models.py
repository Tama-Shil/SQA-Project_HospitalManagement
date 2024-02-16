from django.db import models

class Bed(models.Model):
    
    """
    Model representing a hospital bed.

    :param bedNumber: The number of the bed.
    :type bedNumber: str, max length 20
    :param bedType: The type of the bed.
    :type bedType: str, max length 20, choices: ('general', 'private', 'intensive_care')
    :param isOccupied: Indicates whether the bed is occupied.
    :type isOccupied: bool, default False

    :return: String representation of the bed instance.
    :rtype: str
    """
    BED_TYPES = (
        ('general', 'General'),
        ('private', 'Private'),
        ('intensive_care', 'Intensive Care'),
    )
    
    bedNumber = models.CharField(max_length=20)
    bedType = models.CharField(max_length=20, choices=BED_TYPES)
    isOccupied = models.BooleanField(default=False)
    
    def __str__(self):
        """
            method to return the patient's bedNumber as its string representation.
        """
        return self.bedNumber
    

class Patient(models.Model):
    """
    Model representing a patient in the hospital.

    :param firstName: The first name of the patient.
    :type firstName: str, max length 100
    :param lastName: The last name of the patient.
    :type lastName: str, max length 100
    :param age: The age of the patient.
    :type age: int
    :param gender: The gender of the patient.
    :type gender: str, max length 20, choices: ('male', 'female', 'other')
    :param assignedBed: The bed assigned to the patient.
    :type assignedBed: Bed, on_delete=models.SET_NULL, null=True, blank=True
    :param status: The status of the patient.
    :type status: str, max length 20, default 'Admitted'
    :param GENDER_TYPE: The type of the genders.
    :type GENDER_TYPE: str, max length 20, choices: (('male','female','Other'))

    :return: String representation of the patient instance.
    :rtype: str
    """


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
        """
            method to return the patient's firstName and lastName as its string representation.
        """
        return self.firstName + " " + self.lastName
    
