from django.shortcuts import render
from django.views import generic
from django import views


def homepage(request):
    return render(request, 'home/home.html')