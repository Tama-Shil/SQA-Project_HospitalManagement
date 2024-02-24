# collectReport/forms.py
from django import forms
from .models import Patient

class Report(forms.ModelForm):
    """
    Form for collecting patient report information.

    This form is a ModelForm for the 'Patient' model, allowing users to enter
    patient report information, including patient ID, name, age, gender, and
    various medical test results.
    """

    class Meta:
        model = Patient
        fields = ['patient_id', 'patient_name', 'age', 'gender', 'blood_test', 'x_ray', 'urine_analysis']
