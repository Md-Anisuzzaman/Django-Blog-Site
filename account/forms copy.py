# from django import forms
# from .models import Account

# class RegistrationForm(UserCreationForm):
#     class Meta:
#         model = Account
#         fields = ('username', 'email', 'role', 'phone_number', 'password1', 'password2')

#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if len(username) < 3:
#             raise forms.ValidationError("Username must be at least 3 characters long.")
#         return username

#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if Account.objects.filter(email=email).exists():
#             raise forms.ValidationError("Email already in use.")
#         return email

#     def clean_phone_number(self):
#         phone_number = self.cleaned_data['phone_number']
#         # You can add custom phone number validation here if needed
#         return phone_number

from django import forms
from account.models import RegistrationModel
from django.contrib.auth.hashers import make_password

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    # confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = RegistrationModel
        fields = ['username', 'email', 'role', 'password']

    # def save(self, commit=True):
    #     user = super(RegistrationForm, self).save(commit=False)
    #     user.set_password(self.cleaned_data["password"])
    #     if commit:
    #         user.save()
    #     return user
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.password = make_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


