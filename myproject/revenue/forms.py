from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import calendar
from .models import Applications
Certificate_items=[
('caste','Caste'),
('income','Income'),
('residential','Residential'),
('dob','Date of Birth')
]
class RegistrationForm(UserCreationForm):
  
	email = forms.EmailField(required=True)



	class Meta:
		model = User
		fields=(
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
			)


	def save(self,commit=True):	
		user = super(RegistrationForm,self).save(commit=False)
		user.first_name=self.cleaned_data['first_name']
		user.last_name=self.cleaned_data['last_name']
		user.email=self.cleaned_data['email']

		if commit:
			user.save()

		return user	
						
class Applicationform(forms.ModelForm):
	#Certificates=forms.ModelChoiceField(queryset=Applications.objects.order_by('Certificate').values_list('Certificate', flat=True).distinct())
	class Meta:
		model = Applications
		fields=(
			'Name',
			'SurName',
			'MotherName',
			'FatherName',
			'Certificate',
			)

	
						
					





	