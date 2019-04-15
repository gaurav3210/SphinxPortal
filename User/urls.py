from django.conf.urls import url , include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url('', views.dashboard, name='dashboard'),
    url(r'login_success/$', views.login_success, name='login_success'),
   # url(r'^accounts/profile/$', TemplateView.as_view(template_name='dashboard.html'), name='user_dashboard'),
]