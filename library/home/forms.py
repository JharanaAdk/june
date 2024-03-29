from django import forms 
from . models import Author, User, Contact
from django.contrib.auth.forms import UserCreationForm
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class UserCreationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']
    