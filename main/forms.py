from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	name = forms.CharField()
	surname = forms.CharField()
	date_field = forms.DateField( widget=forms.TextInput(attrs={'type': 'date'}) )                                           

	class Meta:
		model = User
		fields = ("username", "name", "surname", "date_field", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class EditProfileForm(forms.ModelForm):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	picture = forms.ImageField(required=False)
	bio = forms.CharField(widget=forms.TextInput(), max_length=260, required=False)

	def __str__(self):
		return self.user.username

	class Meta:
		model = Profil
		fields = ('picture', 'bio')