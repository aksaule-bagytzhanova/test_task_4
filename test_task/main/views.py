from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import *
from .forms import AnswerForm, StudentRegisterForm


def register_page(request):
    if request.method == "POST":
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = StudentRegisterForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")


def home(request):
    return render(request, 'dashboard.html')


def quizzes_page(request):
    quizzes = Quiz.objects.all()
    context = {'quizzes': quizzes}
    return render(request, 'quizzes_page.html', context)


def quiz_detail_page(request, pk):
    if request.method == 'POST':
        answer_ids = []
        for key, value in request.POST.items():
            if 'question' in key:
                answer_ids.append(int(value))

        correct_answers = len(Answer.objects.filter(id__in=answer_ids, is_correct=True))
        QuizTaker.objects.create(
            student=request.user.student,
            quiz=Quiz.objects.get(id=pk),
            correct_answers=correct_answers
        )

        return redirect('result')
    else:
        quiz = Quiz.objects.get(id=pk)
        context = {'quiz': quiz}
        return render(request, "quiz_detail_page.html", context)


def result_page(request):
    results = QuizTaker.objects.filter(student=request.user.student)
    context = {'results': results}
    return render(request, 'result_page.html', context)
