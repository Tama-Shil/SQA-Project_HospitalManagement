from django.db import models

class PaymentModel(models.Model):
    patientId = models.CharField(max_length = 10, default = "")
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    timeStamp = models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')

    def __str__(self):
        return str(self.id)

    


class Patient(models.Model):
    patient_id = models.CharField(max_length=20)
    patient_name = models.CharField(max_length=100)
    cabin_number = models.IntegerField()
    reports_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    medicine_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cabin_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.patient_name