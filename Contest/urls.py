from django.conf.urls import url , include
from . import views

urlpatterns = [

    url('future_contests',views.future_contests, name='future_contests' ),
    url('create_contest', views.create_contest , name='create_contest'),
    url('contest_register' , views.contest_register , name='contest_register'),
    url('contest', views.Contest, name='contest'),
    url('result', views.result, name='result'),


]