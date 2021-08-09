from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from common.forms import UserForm

from .models import User
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def signup(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('main')
	else:
		form = UserForm()
	return render(request, 'common/signup.html', {'form': form})


@login_required(login_url='common:login')
def account_modify(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	if request.method == 'POST':
		form = CustomUserChangeForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
			return redirect('pybo:main')
	else:
		form = CustomUserChangeForm(instance=user)
	context = {'form': form}
	return render(request, 'common/modify.html', context)


@login_required(login_url='common:login')
def password_modify(request, user_id):
	user = get_object_or_404(User, pk=user_id)

	if request.method == 'POST':
		form = PasswordChangeForm(user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			return redirect('pybo:main')
	else:
		form = PasswordChangeForm(user)
	context = {'form': form, 'user': user}
	return render(request, 'common/password_modify.html', context)
