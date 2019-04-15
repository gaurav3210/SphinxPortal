from django.conf.urls import url, include
from .import views
#from register import views
from django.contrib import admin
from django.urls import path

# SET THE NAMESPACE!
#app_name = 'register'
urlpatterns = [
    url('', views.home, name='register'),
    url(r'login_success/$', views.login_success, name='login_success'),
    #url(r'^user_login/$', views.user_login, name='user_login')
    #url('',views.Main, name='main'),
]
