from django.shortcuts import render

# Create your views here.
def create_contest(request):
    return render(request, 'create_contest.html')


def future_contests(request):
    return render(request , 'future_contests.html')


def contest_register(request):
    return render(request , 'contest_register.html')