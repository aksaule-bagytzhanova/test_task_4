from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'dashboard.html')

def test_page(request):
    return render(request, 'test_page.html')

def result_page(request):
    return render(request, 'result_page.html')