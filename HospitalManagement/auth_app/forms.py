from django import forms
from .models import Hospital_User

class UserForm(forms.ModelForm):
    class Meta:
        model = Hospital_User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'address', 'cell_number', 'user_type']
