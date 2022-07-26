from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    return render(request, 'index.html')


def mentions(request):
    return render(request, 'mentions.html')


def teamoverview(request):
    return render(request, 'teamoverview.html')
