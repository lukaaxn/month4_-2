from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=100)
    confirm_password = forms.CharField(max_length=100)

    def clean_confirm_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise forms.ValidationError('Password and confirm password do not match')
        return self.cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
       