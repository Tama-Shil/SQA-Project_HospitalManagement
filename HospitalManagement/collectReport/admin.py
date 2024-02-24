# collectReport/admin.py
from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Patient model.
    """

    list_display = ('patient_id', 'patient_name', 'age', 'gender', 'blood_test', 'x_ray', 'urine_analysis')
    search_fields = ['patient_id', 'patient_name']

admin.site.register(Patient, PatientAdmin)
