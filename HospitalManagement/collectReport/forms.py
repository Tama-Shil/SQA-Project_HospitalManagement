# collectReport/forms.py
from django import forms
from .models import Patient

class Report(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['patient_id', 'patient_name', 'age', 'gender', 'blood_test', 'x_ray', 'urine_analysis']
