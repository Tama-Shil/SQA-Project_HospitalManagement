from django.contrib import admin
from .models import Patient, Medicine

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'patientId', 'gender', 'cabinNo')

class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name','inStock','price')

admin.site.register(Patient, PatientAdmin)
admin.site.register(Medicine,MedicineAdmin)