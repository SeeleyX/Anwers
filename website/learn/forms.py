from django import forms
from learn.models import *
from django.contrib.auth.models import User

class LearnerUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password', 'email',)

		widgets = {
			'username' : forms.TextInput(attrs={'placeholder' : 'Username'}),
			'password' : forms.PasswordInput(attrs={'placeholder' : 'Password'}),
			'email' : forms.TextInput(attrs={'placeholder' : 'Email'}),
		}

		help_texts = {
			'username' : None,
			'password' : None,
			'email' : None,
		}

		labels = {
			'username' : "",
			'password' : "",
			'email' : "",
		}

	def __init__(self, *args, **kwargs):
		super(LearnerUserForm, self).__init__(*args, **kwargs)
		self.fields['email'].required = False