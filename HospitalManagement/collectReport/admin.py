# collectReport/admin.py
from django.contrib import admin
from .models import PatientReport, MedicalTest

class MedicalTestAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(MedicalTest, MedicalTestAdmin)

class PatientReportAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'patient_name', 'age', 'gender', 'display_tests']

    def display_tests(self, obj):
        return ", ".join([test.name for test in obj.tests.all()])

admin.site.register(PatientReport, PatientReportAdmin)
