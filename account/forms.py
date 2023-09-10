from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter your password'}))

    class Meta:
        model = Account
        fields = ['username', 'email', 'role', 'password']
    def clean(self):
        cleaned_data = super(RegistrationForm,self).clean()
        # username = cleaned_data.get('username')
        # email = cleaned_data.get('email')
        # password = cleaned_data.get('password')
        
        for field_name in ['username', 'email', 'role', 'password']:
            if not cleaned_data.get(field_name):
                self.add_error(field_name, 'This field is required.')
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter username'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email address'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter password'

            
