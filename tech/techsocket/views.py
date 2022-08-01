from email import message
from django.shortcuts import render,redirect
from .models import *
import array as arr
from datetime import datetime
from django.views.decorators.cache import cache_control
import json
import numpy as np
from datetime import datetime
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
        users=UserDetails.objects.filter().exclude(user_id=user)
        l1=[]
        l2=[]
        skills=SkillList.objects.filter()
        for i in skills:
            ans=i.skill_name
            l2.append(ans)
       
        for i in users:
            ans=i.first_name+" "+i.last_name+"("+i.user_id+")"
            l1.append(ans)
        
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
        l12=json.dumps(l2)

        context={
            'userdetails':user_details,
            'posts':l,
            'users_names':l11,
            'skills':l12,
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

def sendrecognition(request):
    if request.method=='POST':
        us=request.session['user_id']
        coins=int(request.POST['coins'])
        coins1=coins
        
        skill=request.POST['skills']
        
        message=request.POST['message']
        user1=request.POST['name'][-7:]
        user=user1[0:6]
        res=UserDetails.objects.filter(user_id=user)
        res1=UserDetails.objects.filter(user_id=us)
        l=""
        for i in res1:
            coins2=i.techie_coins-coins
        posts=Posts.objects.filter()
        post_no=len(posts)+1
        post_no_str=str(post_no)
        for i in res:
            coins+=i.techie_coins
            l=i.skills
            
        if len(l)==0:
            resr=skill
        else:
            resr=l.split(",")
            if skill not in resr:
                l+=","+skill
        
       
        res1=np.array(res)
        UserDetails.objects.filter(user_id=user).update(techie_coins=coins)
        UserDetails.objects.filter(user_id=us).update(techie_coins=coins2)
        UserDetails.objects.filter(user_id=user).update(skills=l)
        Posts.objects.create(post_id=post_no,post=message,id=post_no_str,user_id=us,mentions=user,given_coins=coins1)
        len2=len(UserDetails.objects.filter())
        len1=len(PostSeen.objects.filter())+1
        users2=[]
        res2=UserDetails.objects.filter()
        for x in res2:
            users2.append(x.user_id)
        for i in range(len2):
            len3=str(len1)
            PostSeen.objects.create(post_id=post_no,user_id=users2[i],id=len3,seen="False")
            len1+=1
    return redirect('/index/')
    


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
    if 'logged_in' in request.session:
        ach=Achievements.objects.filter()
        now=datetime.now()
        now_month=now.strftime("%m")
        now_year=now.strftime("%Y")
        l=[]
        h1=int(now_year+now_month)
        print(now_month)
        print(now_year)
        # print(h1)
        for x in ach:
            
            p=x.month
            p1=x.year
            h2=int(p1+p)
            print(h2)
            if(h1==h2):
                print(111)
                d={}
                d['user_id']=x.user_id
                d['achievement']=x.achievement_name
                ach1=UserDetails.objects.filter(user_id=x.user_id)
                for y in ach1:
                    d['name']=y.first_name+" "+y.last_name
                l.append(d)
        data={
            'achievements':l
        }
        return render(request, 'felicitations.html',data)


def awards(request):
    if 'logged_in' in request.session:
        if request.method=='POST':
            
            print(request.POST['award'])
            award=1
            user1=request.POST['name'][-7:]
            user2=user1[0:6]
            x=Nominations.objects.filter(award_id=award)
            c=0
            for i in x:
                c=i.no_of_nominations
            c+=1
            Nominations.objects.filter(award_id=award).update(no_of_nominations=c)
            x1=Nominate.objects.filter(award_id=award)
            if len(x1)==0:
                Nominate.objects.create(award_id=award,user_id=user2,id=1,no_of_nominations=1)
            else:
                x2=Nominate.objects.filter(award_id=award,user_id=user2)
                if len(x2)==0:
                    Nominate.objects.create(award_id=award,user_id=user2,id=1,no_of_nominations=1)
                else:
                    Nominate.objects.filter(award_id=award,user_id=user2).update(no_of_nominations=len(x2)+1)

        date_now=datetime.now()
        date_present=date_now.strftime("%m/%d/%Y")
        nominations=Nominations.objects.filter()
        user=request.session['user_id']
        users=UserDetails.objects.filter().exclude(user_id=user)
        l=[]
        for x in nominations:
            d={}
            d['award_name']=x.award_name
            d['nominated']=x.no_of_nominations
            l.append(d)
        l1=[]
        for i in users:
            ans=i.first_name+" "+i.last_name+"("+i.user_id+")"
            l1.append(ans)
        l11=json.dumps(l1)
        data={
            'awards':l,
            'users_names':l11
        }
        return render(request, 'awards.html',data)


def talentassesments(request):
    return render(request, 'talentassesments.html')


def rewards(request):
    return render(request, 'rewards.html')


def feedback(request):
    return render(request, 'feedback.html')

#yess
def goals(request):
    print("oooo")
    if request.session=='POST':
        print("yeahhhh")
    return render(request, 'goals.html')

def queries(request):
    return render(request, 'queries.html')


def personaldm(request):
    return render(request, 'personaldm.html')


def techquery(request):
    return render(request, 'techquery.html')
