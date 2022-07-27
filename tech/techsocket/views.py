from django.shortcuts import render,redirect
from .models import *
# Create your views here.
import cv2
from django.views.decorators.cache import cache_control
import json
@cache_control(no_cache=True, must_revalidate=True)
def login(request):
    if request.method=='POST':
        user_email=request.POST['mail']
        user_pwd=request.POST['pswd']
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
        user=request.session['user_id']
        user_details=UserDetails.objects.filter(user_id=user)
        posts=Posts.objects.filter()
        users=UserDetails.objects.filter()
        l1=[]
        for i in users:
            ans=i.first_name+" "+i.last_name+"("+i.user_id+")"
            l1.append(ans)
        print(l1)
        l=[]
        for x in posts:
            r=x.post_id
            r1=PostSeen.objects.filter(user_id=user)
            
            for y in r1:
                if y.post_id==r and y.seen=="False":
                    d={}
                    pr=UserDetails.objects.filter(user_id=x.user_id)
                    pr1=UserDetails.objects.filter(user_id=x.mentions)
                    for p in pr:
                        d['user_name']=p.first_name+" "+p.last_name
                    for p1 in pr1:
                        d['mention']=p1.first_name+" "+p1.last_name
                    d['post']=x.post
                    l.append(d)
        PostSeen.objects.filter(user_id=user).update(seen="True")
        l11=json.dumps(l1)
        print(l11)
        context={
            'userdetails':user_details,
            'posts':l,
            'users_names':l11
            }
        return render(request, 'index.html',context)
    return redirect('/')

def mentions(request):
    if 'logged_in' in request.session:
        user=request.session['user_id']
        mentioned=Posts.objects.filter(mentions=user)
        r=UserDetails.objects.filter(user_id=user)
        for x in r:
 
            ans=x.first_name+" "+x.last_name
        l=[]
        for x in mentioned:
            d={}
            r1=UserDetails.objects.filter(user_id=x.user_id)
            d['mention']=ans
            d['post']=x.post
            for y in r1:
                d['user_name']=y.first_name+" "+y.last_name

            l.append(d)

        context={
            'posts':l
        }
    return render(request, 'mentions.html',context)

def teamoverview(request):
    if 'logged_in' in request.session:
        user=request.session['user_id']
        team=Team.objects.filter()
        l=[]

        for x in team:
            if user in x.members_list:
                l=x.members_list
        l1=[]
        sum=1
        for x in l:
            p=UserDetails.objects.filter(user_id=x)
            d={}
            d['no']=sum
            for y in p:
                
                if 'LinkedIn' in y.social_media:
                        d['LinkedIn']=y.social_media['LinkedIn']
                d['user_name']=y.first_name+" "+y.last_name
                d['designation']=y.designation
                d['join_month']=y.join_month
                d['join_date_no']=y.join_date_no
                d['join_year']=y.join_year
            l1.append(d)
            
        context={
                'team':l1
        }
        return render(request, 'teamoverview.html',context)


def people(request):
    if 'logged_in' in request.session:
        user_details=UserDetails.objects.filter()
        context={
            'users':user_details
        }
        return render(request, 'people.html',context)


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
