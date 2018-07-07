from django.forms import ModelForm
from django import  forms
from myfirst_app.models import RegistrationModel

class RegistrationForm(ModelForm):
    class Meta:
        model = RegistrationModel
        fields = '__all__'

class Login_form(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
