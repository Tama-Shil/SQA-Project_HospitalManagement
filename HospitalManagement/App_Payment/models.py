from django.db import models

class PaymentModel(models.Model):
    patientId = models.CharField(max_length = 10, default = "")
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    timeStamp = models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')

    def __str__(self):
  
        return f"Payment #{self.id}"