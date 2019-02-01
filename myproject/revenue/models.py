from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


	
class Applications(models.Model):

	Name = models.CharField(max_length=20)
	SurName = models.CharField(max_length=50)
	FatherName=  models.CharField(max_length=20)
	MotherName=models.CharField(max_length=50)
	Certificate=models.CharField(max_length=50)	

	def __unicode__(self):
		return self.Name

# Create your models here.
#label="Select Certificate",widget=models.Select(choices=Certificate_items)