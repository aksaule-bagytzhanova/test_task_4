from os import name
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('registration/', views.register_page, name="registration"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_request, name="logout"),

    path('quizzes/', views.quizzes_page, name="quizzes"),
    path('quizzes/<int:pk>', views.quiz_detail_page, name="quiz-detail"),
    path('result_page/', views.result_page, name="result"),


]