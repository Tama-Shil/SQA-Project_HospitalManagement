from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'patient_name', 'cabin_number', 'reports_bill', 'medicine_bill', 'cabin_bill', 'total_bill')

