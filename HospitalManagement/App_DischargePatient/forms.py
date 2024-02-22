from django import forms
from .models import Patient

class DischargeForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['patientId']
