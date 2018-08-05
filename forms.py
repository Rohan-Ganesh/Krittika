from django import forms
from home.models import *  

class HomeForm(forms.ModelForm):
  name = forms.CharField(widget=forms.TextInput(), max_length = 50)
  email = forms.EmailField(required = True, max_length = 50)
  feedback = forms.CharField(widget=forms.TextInput(), max_length = 200)
  class Meta:
    model = Post
    fields = ['name','email','feedback']
               
               
               
