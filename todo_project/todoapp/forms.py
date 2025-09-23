from django import forms
from django.contrib.auth.models import User

# register ofrm
class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]#colunms in user table that we use in the form


class UserLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]