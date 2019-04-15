from django.shortcuts import render,reverse
from django.shortcuts import redirect, HttpResponseRedirect
# Create your views here.
def dashboard(request):
    return render(request , 'dashboard.html')



def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    if request.user.is_staff:
        # user is an admin
        return HttpResponseRedirect(reverse("register"))