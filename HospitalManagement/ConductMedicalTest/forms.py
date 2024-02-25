# forms.py
from django import forms
from .models import TestRecord

class TestRecordForm(forms.ModelForm):
    class Meta:
        model = TestRecord
        exclude = ['test_record_number']  # Exclude the test_record_number field from the form
