from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import  render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from datetime import datetime

from .forms import *
from .models import *


# Create your views here.

def homepage(request):
    return HttpResponse('<html><body><h1>POCETAK INFSTAGRAM</h1></body></html>')

@login_required
def profil(request):
	profile_list = Profile.objects.all()
	post_list = Post.objects.order_by('-post_time')
	user_list = User.objects.all()
	context = {'profile_list': profile_list, 'post_list': post_list, 'user_list': user_list}
	return render(request, 'profil.html', context=context)

def register_user(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:profile")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, 'register.html', context={"register_form":form})

def login_user(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, "You are now logged in as {username}.")
				return redirect("main:profile")
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
def password_change(request):
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

def password_change_done(request):
	return render(request, 'change_password_successful.html')


@login_required
@transaction.atomic
def edit_profile(request):
    if request.method == 'POST':
        profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('/profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        profile_form = EditProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', { 'profile_form': profile_form })


def NewPost(request):
	files_objs = []
	posts = Post.objects.all()
	obj = request.POST.get('likes')

	if request.method == 'POST':
		form = NewPostForm(request.POST, request.FILES, instance=request.user.profile)
		if form.is_valid():
			files = request.FILES.getlist('post_image')
			caption = form.cleaned_data.get('post_description')
			time = datetime.now()
			profile_id = request.user.profile.id
			
			for file in files:
				file_instance = Post(post_image=file,  post_time=time,  profile_post_id = profile_id )
				files_objs.append(file_instance)

			p = Post.objects.get_or_create(post_image=file, post_description=caption,  post_time=time, profile_post_id = profile_id)
			p[0].save()
			return redirect('main:homepage')
	else:
		form = NewPostForm(instance=request.user.profile)

	context = {'form':form}

	return render(request, 'nova_objava.html', context)


def home(request):
	user = request.user
	post_list = Post.objects.order_by('-post_time')
	profile_list = Profile.objects.all()
	user_list = User.objects.all()
	comment_list = Comment.objects.all()
	context = {'post_list': post_list, 'profile_list': profile_list, 'user_list': user_list, 'comment_list': comment_list, 'user':user}
	return render(request, 'home.html', context=context)


@login_required
def like(request, post_id):
	user = request.user
	post = Post.objects.get(id=post_id)
	current_likes = post.likes
	liked = Likes.objects.filter(user=user, post=post).count()

	if not liked:
		like = Likes.objects.create(user=user, post=post)
		current_likes = current_likes + 1

	else:
		Likes.objects.filter(user=user, post=post).delete()
		current_likes = current_likes - 1

	post.likes = current_likes
	post.save()

	return HttpResponseRedirect(reverse('main:home'))


@login_required
def comment(request, post_id):
	user = request.user

	if request.method == 'POST':
		form = NewCommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post_id = post_id
			comment.user = user
			form.save()
		return redirect('main:home')
	else:
		form = NewCommentForm(request.GET)
	
	context = {'user':user, 'form':form, 'post_id': post_id}
	return render(request, 'comment.html', context)

def delete_comment(request, k_id):
	user = request.user
	comment = Comment.objects.get(id=k_id)
	Comment.objects.filter(user=user, comment=comment).delete()
	return HttpResponseRedirect(reverse('main:home'))


def redirect_view(request):
    response = redirect('/home')
    return response