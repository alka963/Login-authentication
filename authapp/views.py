from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from .forms import LoginForm, RegistrationForm      

def signin(request):
	forms = LoginForm()
	if request.method == 'POST':
		forms = LoginForm(request.POST)
		if forms.is_valid():
			email = forms.cleaned_data['email']
			password = forms.cleaned_data['password']
			user = authenticate(email=email, password=password)
			if user:
				login(request, user)
				return redirect('home')
	context = {
		'form': forms
	}
	return render(request, 'signin.html', context)

def signup(request):
	forms = RegistrationForm()
	if request.method == 'POST':
		forms = RegistrationForm(request.POST)
		if forms.is_valid():
			email = forms.cleaned_data['email']
			username = forms.cleaned_data['username']
			password = forms.cleaned_data['password']
			confirm_password = forms.cleaned_data['confirm_password']
			address =forms.cleaned_data['address']
			if password == confirm_password:
				try:
					User.objects.create_user(username=username, password=password, confirm_password=confirm_password, email=email, address=address)
					return redirect('signin')
				except:
					context = {
						'form': forms,
						'error': 'This Username Already exists!'
					}
					return render(request, 'signup.html', context)
	context = {
		'form': forms
	}
	return render(request, 'signup.html', context)

def signout(request):
	logout(request)
	return redirect('signin')