from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
  # Since the default form does not have email, now we added this 
  email = forms.EmailField()
  
  class Meta:
    model = User
    fields = ['username','email', 'password1', 'password2']

  def __init__(self, *args, **kwargs):
    super(UserCreationForm, self).__init__(*args, **kwargs)

    # Change error messages and hide the help_text
    # For aethestical reasons
    for fieldname in ['username','email', 'password1', 'password2']:
      self.fields[fieldname].help_text = None
      self.fields[fieldname].error_messages = {'required':'Required'}

class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['image']