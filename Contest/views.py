from django.shortcuts import render
from .models import *
# Create your views here.
def create_contest(request):
    return render(request, 'create_contest.html')


def future_contests(request):
    future = contest.objects.all()
    context = {'future': future}
    return render(request , 'future_contests.html', context)


def contest_register(request):
    return render(request , 'contest_register.html')


def Contest(request):
    all_questions = question.objects.filter(contestID="1")
    context={'all_questions': all_questions}
    return render(request, "choice question.html",context);

def result(request):
    return render(request,'RESULT.html');