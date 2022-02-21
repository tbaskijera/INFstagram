from django.http import HttpResponse
from django.shortcuts import  render, redirect, HttpResponseRedirect
from .forms import *
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth import update_session_auth_hash
from django.db import transaction
# Create your views here.

from django.contrib.auth import logout



def homepage(request):
    return HttpResponse('<html><body><h1>POCETAK INFSTAGRAM</h1></body></html>')

@login_required
def profil(request):
	lista_nova = Profil.objects.all()
	context = {'lista_nova': lista_nova}
	return render(request, 'profil.html', context=context)

def registration(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, 'register.html', context={"register_form":form})

def loginuser(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, "You are now logged in as {username}.")
				#return redirect("main:homepage")
				return redirect("main:profil")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, 'login.html' , context={"login_form":form})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/login')

@login_required
def PasswordChange(request):
	user = request.user
	if request.method == 'POST':
		form = ChangePasswordForm(request.POST)
		if form.is_valid():
			new_password = form.cleaned_data.get('new_password')
			user.set_password(new_password)
			user.save()
			update_session_auth_hash(request, user)
			return redirect('change_password_done')
	else:
		form = ChangePasswordForm(instance=user)
	return render(request, 'change_password.html', context = {'change_form':form})

def PasswordChangeDone(request):
	return render(request, 'change_password_successful.html')


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        #user_form = NewUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profil)
        if profile_form.is_valid(): # && user_form.is_valid()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('/homepage')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        #user_form = NewUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profil)
    return render(request, 'edit_profile.html', {#'user_form': user_form, 
	'profile_form': profile_form })
