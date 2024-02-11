from django import forms

class advancePaymentForm(forms.Form):
    advancepatientId = forms.CharField(label='Patient ID', required= True)
    advanceTotalAmount = forms.DecimalField(label='Advance amount', min_value=0.01, required= True)


class emiPaymentForm(forms.Form):
    emipatientId = forms.CharField(label='Patient ID', required= True)
    emitTotalAmount = forms.DecimalField(label='EMI Amount', min_value=0.01, required= True)
    emiTimeStamp = forms.DateField(label='EMI Pay Date', input_formats=['%Y-%m-%d'], help_text='Format: YYYY-MM-DD')

