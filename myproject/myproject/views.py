from django.shortcuts import render,redirect

def home(request):
	return redirect('/firstapp/home/')
