"""
Module: forms

Description:
This module defines the form classes used in the hospital management system.

Classes:
    - TestRecordForm: Form for creating and updating test records.
"""

from django import forms
from .models import TestRecord

class TestRecordForm(forms.ModelForm):
    """
    Form for creating and updating test records.

    Inherits from:
        forms.ModelForm

    Attributes:
        Meta (class): Inner class defining metadata options for the form.
    """
    class Meta:
        """
        Metadata options for the TestRecordForm.

        Attributes:
            model (Model): The model associated with the form.
            exclude (list): List of fields to exclude from the form.
        """
        model = TestRecord
        exclude = ['test_record_number']  # Exclude the test_record_number field from the form
