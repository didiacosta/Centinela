from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Usuario 

class EditarClaveForm(forms.Form):
	actual_password = forms.CharField(
        label='Clave actual:',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password = forms.CharField(
        label='Nueva clave:',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	password2 = forms.CharField(
        label='Repetir clave:',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	def clean_password2(self):
		#Comprueba que password y password2 sean iguales.
		password = self.cleaned_data['password']
		password2 = self.cleaned_data['password2']
		if password != password2:
			raise forms.ValidationError('La confirmacion de la clave no coincide.')
		return password2