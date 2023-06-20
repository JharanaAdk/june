from django import forms 
from . models import Author, User
from django.contrib.auth.forms import UserCreationForm
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class UserCreationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']
    