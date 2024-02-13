from django import forms
from .models import Bed, Patient


class BedForm(forms.ModelForm):
    
    class Meta:
        model = Bed
        fields = '__all__'


class PatientForm(forms.ModelForm):
    
    class Meta:
        model = Patient
        fields = '__all__'