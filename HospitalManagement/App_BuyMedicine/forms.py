from django import forms


class PatientIDForm(forms.Form):
    patient_id = forms.CharField(label='Enter Patient ID', max_length=10)

