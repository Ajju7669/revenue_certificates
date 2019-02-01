from django.shortcuts import render

from revenue.forms import RegistrationForm,Applicationform
from django.views.generic import ListView,TemplateView
from django.contrib.auth.decorators import login_required
from .models import Applications
from django.contrib.auth.models import User
from urllib.parse import urlparse
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
#from .special_func import get_next_url
from django.template.context_processors import csrf
from django.views import View
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
    
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
"""def index(request):
	form=Registrationform()
	context={
		"myregister":formA
	}
	return render(request,"myproject/index.html",context)"""

def home(request):

	return render(request,"myproject/home.html")
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('firstapp/home/')
    else:
        form = RegistrationForm()
    return render(request,'myproject/register.html',{'form':form})

    
"""def apply(request):
    if request.method=='POST':
        form=Applications(request.POST)
        if form.is_valid():
            name1=forms.cleaned_data['Name']
            Fname1=formsr.cleaned_data['FatherName']
            return redirect('firstapp/home/')
           # form=Applications()
    args={'form':form,'name1':name1,'Fname':Fname1}
    return render(request,'myproject/apply.html',args)"""
class HomeView(TemplateView):
    template_name='myproject/apply.html'
    

    def get(self,request):
        form=Applicationform()       
        return render(request,self.template_name,{'form':form})

    def post(self,request):
            form = Applicationform(request.POST)
            if form.is_valid():
                form.save()
                Name= form.cleaned_data['Name']
                FatherName = form.cleaned_data['FatherName']
                MotherName= form.cleaned_data['MotherName']
                Certificate= form.cleaned_data['Certificate']
               
            args={'form': form,'Name':Name,'FatherName':FatherName,'MotherName':MotherName,'Certificate':Certificate}
            return render(request, self.template_name,args)



def index(request):
        list1=Applications.objects.all()
        return render(request,'myproject/mro.html',{'list1':list1})


""""def officerlogin(request):
    if request.method == 'POST':
        form = OfficerLogin(request.POST)
        if form.is_valid():
            
            return redirect('firstapp/home/')
    else:
        form = RegistrationForm()
    return render(request,'myproject/register.html',{'form':form})"""

       
def logins(request):

    return render(request,"myproject/officerlogins.html")
"""class ELoginView(View):

    def get(self, request):
        # if the user is logged in, then do a redirect to the home page
        if auth.get_user(request).is_authenticated:
            return redirect('firstapp/mro')
        else:
            # Otherwise, form a context with the authorization form 
            # and we return to this page context.
            # It works, for url - /admin/login/ and for /accounts/login/ 
            context = create_context_username_csrf(request)
            return render_to_response('firstapp/mrologin/', context=context)
 
    def post(self, request):
        # having received the authorization request
        form = AuthenticationForm(request, data=request.POST)
 
        # check the correct form, that there is a user and he entered the correct password
        if form.is_valid():
            # if successful authorizing user
            auth.login(request, form.get_user())
            # get previous url
            next = urlparse(get_next_url(request)).path
            # and if the user of the number of staff and went through url /admin/login/
            # then redirect the user to the admin panel
            if next == '/admin/login/' and request.user.is_staff:
                return redirect('/admin/')
            # otherwise do a redirect to the previous page,
            # in the case of a / accounts / login / will happen is another redirect to the home page
            # in the case of any other url, will return the user to the url
            return redirect(next)
 
        # If not true, then the user will appear on the login page
        # and see an error message
        context = create_context_username_csrf(request)
        context['login_form'] = form
 
        return render_to_response('firstapp/mrologin', context=context)
 
 
# helper method to generate a context csrf_token
# and adding a login form in this context
def create_context_username_csrf(request):
    context = {}
    context.update(csrf(request))
    context['login_form'] = AuthenticationForm
    return context"""
"""def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('firstapp/home/')
    return render_to_response('myproject/mrologin.html', context_instance=RequestContext(request))"""
def mro_xyz(request):
    return render(request,"myproject/mroxyz.html")