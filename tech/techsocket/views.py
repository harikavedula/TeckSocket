from django.shortcuts import render,redirect
from .models import *

# Create your views here.
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True)
def login(request):
    if request.method=='POST':
        user_email=request.POST['mail']
        user_pwd=request.POST['pswd']
        print(user_email)
        print(user_pwd)
        Users=User.objects.all()
        for x in Users:
            if x.email==user_email and x.password==user_pwd:
                request.session['logged_in']=True
                request.session['user_id']=x.user_id
                return redirect('/index/')
    return render(request,'login.html')

def logout(request):
    del request.session['logged_in']
    del request.session['user_id']
    return redirect('/')

def index(request):
    if 'logged_in' in request.session:
        return render(request, 'index.html')
    return redirect('/')

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


def personaldm(request):
    return render(request, 'personaldm.html')


def techquery(request):
    return render(request, 'techquery.html')
