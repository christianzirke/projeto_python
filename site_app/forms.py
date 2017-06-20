from django import forms

class UserRegistrationForm(forms.Form):
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )

class UserRegistrationForm(forms.Form):
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )