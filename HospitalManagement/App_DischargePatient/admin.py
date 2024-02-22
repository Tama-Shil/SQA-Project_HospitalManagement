from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'patientId', 'gender', 'cabinNo', 'totalBill','paymentPaid' )