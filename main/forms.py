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

	class Meta:
		model = User
		fields = ("username", "name", "surname", "date_field", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class ChangePasswordForm(forms.ModelForm):
	id = forms.CharField(widget=forms.HiddenInput())
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input is-medium'}), label="Old password", required=True)
	new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input is-medium'}), label="New password", required=True)
	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input is-medium'}), label="Confirm new password", required=True)

	class Meta:
		model = User
		fields = ('id', 'old_password', 'new_password', 'confirm_password')

	def clean(self):
		super(ChangePasswordForm, self).clean()
		id = self.cleaned_data.get('id')
		old_password = self.cleaned_data.get('old_password')
		new_password = self.cleaned_data.get('new_password')
		confirm_password = self.cleaned_data.get('confirm_password')
		user = User.objects.get(pk=id)
		if not user.check_password(old_password):
			self._errors['old_password'] =self.error_class(['Old password do not match.'])
		if new_password != confirm_password:
			self._errors['new_password'] =self.error_class(['Passwords do not match.'])
		return self.cleaned_data


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'profile_image')


class NewPostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('post_image', 'post_description')


class NewCommentForm(forms.ModelForm):
	comment = forms.CharField(max_length=500)
	title = forms.CharField(max_length=100)

	class Meta:
		model = Comment
		fields = ('comment', 'title')