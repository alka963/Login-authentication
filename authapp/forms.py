from django import forms

class LoginForm(forms.Form):
	email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'email', 'name': 'email', 'pslaceholder': 'Type your email'}))
	password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'password', 'placeholder': 'Type your password'}))

class RegistrationForm(forms.Form):
	email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'email', 'name': 'email', 'placeholder': 'Type your email'}))
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'username', 'placeholder': 'Type your username'}))
	password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'password', 'placeholder': 'Type your password'}))
	confirm_password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'confirm-password', 'placeholder': 'Type your password again'}))
	address = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'addess','placeholder': 'Type your address'}))