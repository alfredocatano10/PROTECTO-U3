from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import baterias, filtros, aceites, Comment
from django.contrib.auth.models import User


class CustomUserForm (UserCreationForm):
	
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class BatForm (forms.ModelForm):
	
	class Meta:
		model = baterias
		fields = '__all__'

class FilForm (forms.ModelForm):
	
	class Meta:
		model = filtros
		fields = '__all__'

class AceForm (forms.ModelForm):

	class Meta:
		model = aceites
		fields = '__all__'

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)