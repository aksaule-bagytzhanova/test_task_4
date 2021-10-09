from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'dashboard.html')

def test_page(request):
    all_tests = Question.objects.all()
    all_answers = Answer.objects.all()

    context = {'all_tests': all_tests, 'all_answers': all_answers}
    return render(request, 'test_page.html',context)


def result_page(request):
    all_answers = Answer.objects.all()
    context = {'all_answers': all_answers}
    return render(request, 'result_page.html', context)