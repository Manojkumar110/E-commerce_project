from django.contrib.auth .forms import UserCreationForm ,AuthenticationForm
from django import forms
from django.contrib.auth.models import User 

class CustomerCreationForm(UserCreationForm):
    username = forms.EmailField(required=True , label='Email')
    first_name = forms.CharField(required=True, label='First Name')
    last_name = forms.CharField(required=True, label='Last Name')
    class Meta:
       model = User
       fields = ['username','first_name','last_name']
 
class CustomerAuthForm(AuthenticationForm):
    username = forms.EmailField(required=True , label='Email')
