from os import name
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('test_page/', views.test_page, name="test"),
    path('result_page/', views.result_page, name="result"),

]