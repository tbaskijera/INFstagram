from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	name = forms.CharField()
	surname = forms.CharField()
	date_field = forms.DateField( widget=forms.TextInput(attrs={'type': 'date'}))
	#profile_picture = forms.ImageField(upload_to = "images/")      
	bio = forms.CharField( max_length = "260", widget=forms.Textarea(attrs={'cols': 40, 'rows': 6}))                                     

	class Meta:
		model = User
		fields = ("username", "name", "surname", "date_field", "email", "bio", "password1", "password2")
		# maknut "profile_picture"
		
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user