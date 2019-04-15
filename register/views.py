from django.shortcuts import render
from django.shortcuts import HttpResponse
#from register.forms import UserForm, UserProfileInfoForm
#from django.contrib.auth import authenticate, login, logout
#from django.http import HttpResponseRedirect, HttpResponse
#from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,reverse
from django.shortcuts import redirect, HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, 'index.html')

def Main(request):
    return render(request, "Main.html");

@login_required
def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    if request.user.is_superuser:
        # user is an admin
        return HttpResponseRedirect(reverse("create_contest"));
    else:
        return redirect(reverse("dashboard"));


