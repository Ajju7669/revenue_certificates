from  django.conf.urls import url
from django.contrib.auth.views import login,logout
from . import views
from .views import register,HomeView,home,index,logins,mro_xyz
urlpatterns=[
	url(r'home/$',views.home,name='home'),
	url(r'apply/$',HomeView.as_view(),name='apply'),
	url(r'login/$',login,{'template_name':'myproject/login.html'}),
	url(r'logout/$',logout,{'template_name':'myproject/logout.html'}),
	url(r'register/$',register,name='register'),
	url(r'mro/$',views.index,name='mro'),
	url(r'officerlogins/$',views.logins,name='officerlogins'),
	url(r'mro_xyz/$',views.mro_xyz,name='mro_xyz')
	]
