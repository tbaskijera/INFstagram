from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
