from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    return render(request, 'index.html')


def mentions(request):
    return render(request, 'mentions.html')


def teamoverview(request):
    return render(request, 'teamoverview.html')


def people(request):
    return render(request, 'people.html')


def incentives(request):
    return render(request, 'incentives.html')


def felicitations(request):
    return render(request, 'felicitations.html')


def awards(request):
    return render(request, 'awards.html')


def talentassesments(request):
    return render(request, 'talentassesments.html')


def rewards(request):
    return render(request, 'rewards.html')


def feedback(request):
    return render(request, 'feedback.html')


def goals(request):
    return render(request, 'goals.html')

def queries(request):
    return render(request, 'queries.html')