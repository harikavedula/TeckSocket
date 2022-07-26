from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    user=User.objects.all()
    for x in user:
        print(x)
        print(x.email)
    return render(request, 'index.html')


def mentions(request):
    return render(request, 'mentions.html')


def teamoverview(request):
    return render(request, 'teamoverview.html')


def people(request):
    return render(request, 'people.html')
