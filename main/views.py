from datetime import date, datetime
from django.http import HttpResponse
from django.shortcuts import  render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth import update_session_auth_hash
from django.db import transaction
# Create your views here.

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


def NewPost(request):
	user = request.user
	files_objs = []
	objava = Objava.objects.all()
	obj = request.POST.get('lajk_objava')

	if request.method == 'POST':
		form = NewPostForm(request.POST, request.FILES, instance=request.user.profil)
		if form.is_valid():
			files = request.FILES.getlist('slika_objava')
			caption = form.cleaned_data.get('opis_objava')
			
			time = datetime.now()
			#like = 10

			for like in objava:
				if(like.id == obj):
					like.lajk_objava += 1
					like.save()

			profilic = request.user.profil.id
			print(profilic)
			
			for file in files:
				file_instance = Objava(slika_objava=file,  vrijeme_objava=time,  profil_objava_id = profilic )
				#profil_objava=user,
				#file_instance.save()
				files_objs.append(file_instance)

			p = Objava.objects.get_or_create(slika_objava=file, opis_objava=caption,  vrijeme_objava=time, profil_objava_id = profilic)
			#profil_objava=user,
			#p.content.set(files_objs)
			print(p)
			p[0].save()
			return redirect('main:homepage')
	else:
		form = NewPostForm(instance=request.user.profil)

	context = {'form':form}

	return render(request, 'nova_objava.html', context)


def home(request):
	#lista_nova = Objava.objects.all()
	# - je za postavljanje objava od najnovijih do najstarijih
	lista_objava = Objava.objects.order_by('-vrijeme_objava')
	#lista_objava = Objava.objects.all()
	lista_profil = Profil.objects.all()
	lista_useri = User.objects.all()
	context = {'lista_objava': lista_objava, 'lista_profil': lista_profil, 'lista_useri': lista_useri}
	return render(request, 'home.html', context=context)


def novikomentar(request, objava_id):

	post = get_object_or_404(Objava, id=objava_id)
	user = request.user 
	komentar = None

	komentari = post.comments
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			komentar = form.save(commit=False)
			komentar.post = post
			komentar.user = user
			komentar.save()
	else:
		form = CommentForm()
	
	context = {'post': post,
                   'comments': komentari,
                   'new_comment': komentar,
                   'comment_form': CommentForm}

	return render(request, 'comment.html', context)


@login_required
def like(request, o_id):
	user = request.user
	post = Objava.objects.get(id=o_id)
	current_likes = post.likes
	liked = Likes.objects.filter(user=user, post=post).count()

	if not liked:
		like = Likes.objects.create(user=user, post=post)
		#like.save()
		current_likes = current_likes + 1

	else:
		Likes.objects.filter(user=user, post=post).delete()
		current_likes = current_likes - 1

	post.likes = current_likes
	post.save()

	return HttpResponseRedirect(reverse('main:home'))
