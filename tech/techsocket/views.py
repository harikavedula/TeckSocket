from email import message
from pydoc_data.topics import topics
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
                        d['mention_user_id']=p.user_id
                    for p1 in pr1:
                        d['mention']=p1.first_name+" "+p1.last_name
                        
                    d['post']=x.post
                    l.append(d)
        PostSeen.objects.filter(user_id=user).update(seen="True")
        l11=json.dumps(l1)
        l12=json.dumps(l2)
        ans1=Notifications.objects.filter(user_id=user)
        ln=[]
        for x in ans1:
            d={}
            d['notification']=x.notification
            d['msg']=x.notification_message
            ln.append(d)
        if(len(l)==0):
            b=True
        else:
            b=False
        context={
            'userdetails':user_details,
            'posts':l,
            'users_names':l11,
            'skills':l12,
            'notification':ln,
            'truth_val':b
            }
        print(context['notification'])

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
        
        user_details=UserDetails.objects.filter(user_id=user)
        for x in mentioned:
            d={}
            r1=UserDetails.objects.filter(user_id=x.user_id)
            d['mention']=ans
            d['post']=x.post
            d['post_id']=x.post_id
            for y in r1:
                d['user_name']=y.first_name+" "+y.last_name
            d['mention_user_id']=x.user_id
            lln=[]
            comments=PostReplies.objects.filter(post_id=x.post_id)
            for r in comments:
                lln.append(r.reply)
            
            d['comments']=lln
            l.append(d)
            print(l)
        ans1=Notifications.objects.filter(user_id=user)
        ln=[]
        for x in ans1:
            d={}
            d['notification']=x.notification
            d['msg']=x.notification_message
            ln.append(d)
        context={
            'userdetails':user_details,
            'posts':l,
            'notification':ln,
        }
    return render(request, 'mentions.html',context)

def teamoverview(request):
    if 'logged_in' in request.session:
        user=request.session['user_id']
       
        user_details=UserDetails.objects.filter(user_id=user)
        team=Team.objects.filter()
        l=[]

        for x in team:
            if user in x.members_list:
                l=x.members_list
                ppp=x.team_id
        l1=[]
        sum=1
        for x in l:
            p=UserDetails.objects.filter(user_id=x)
            d={}
            d['no']=sum
            for y in p:
                
                d['user_id']=y.user_id
                d['user_name']=y.first_name+" "+y.last_name
                d['designation']=y.designation
                d['join_month']=y.join_month
                d['join_date_no']=y.join_date_no
                d['join_year']=y.join_year
            l1.append(d)
        ans1=Notifications.objects.filter(user_id=user)
        users=UserDetails.objects.filter().exclude(user_id=user)
        l3=[]
        l2=[]
        skills=SkillList.objects.filter()
        for i in skills:
            ans=i.skill_name
            l2.append(ans)
       
        for i in users:
            ans=i.first_name+" "+i.last_name+"("+i.user_id+")"
            l3.append(ans)
        l11=json.dumps(l3)
        l12=json.dumps(l2)
        ln=[]
        for x in ans1:
            d={}
            d['notification']=x.notification
            d['msg']=x.notification_message
            ln.append(d)
        team_goals=TeamGoals.objects.filter(team_id=ppp)
        context={
            'users_names':l11,
            'skills':l12,
            'userdetails':user_details,
                'team':l1,
                'notification':ln,
                'team_goals':team_goals
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
            user_name=i.first_name+" "+i.last_name
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
        len3=len(Notifications.objects.filter())+1
        msg=user_name+" Recognised you"
        msg1="You are mentioned"
        Notifications.objects.create(notification_id=len3,notification=msg1,notification_message=msg,user_id=user,truth_value="False")
    return redirect('/index/')
    


def people(request):
    
    if 'logged_in' in request.session:
        users_details=UserDetails.objects.filter()
        user=request.session['user_id']
        user_details=UserDetails.objects.filter(user_id=user)
        ans1=Notifications.objects.filter(user_id=user)
        ln=[]
        for x in ans1:
            d={}
            d['notification']=x.notification
            d['msg']=x.notification_message
            ln.append(d)
        users=UserDetails.objects.filter().exclude(user_id=user)
        l3=[]
        l2=[]
        skills=SkillList.objects.filter()
        for i in skills:
            ans=i.skill_name
            l2.append(ans)
       
        for i in users:
            ans=i.first_name+" "+i.last_name+"("+i.user_id+")"
            l3.append(ans)
        l11=json.dumps(l3)
        l12=json.dumps(l2)
        context={
            'users_names':l11,
            'skills':l12,
            'userdetails':user_details,
            'users':users_details,
            'notification':ln
        }
        return render(request, 'people.html',context)


def incentives(request):
    if 'logged_in' in request.session:
        user=request.session['user_id']
        user_details=UserDetails.objects.filter(user_id=user)
        ans1=Notifications.objects.filter(user_id=user)
        ln=[]
        for x in ans1:
            d={}
            d['notification']=x.notification
            d['msg']=x.notification_message
            ln.append(d)
        
        inc=Incentives.objects.filter()
        for x in inc:
            print(x.incentive)
        context={
            'userdetails':user_details,
                'incentives':inc,
                'notification':ln,
        }
    return render(request, 'incentives.html',context)


def felicitations(request):
    if 'logged_in' in request.session:
        user=request.session['user_id']
        user_details=UserDetails.objects.filter(user_id=user)
        ach=Achievements.objects.filter()
        now=datetime.now()
        now_month=now.strftime("%m")
        now_year=now.strftime("%Y")
        l=[]
        h1=int(now_year+now_month)
        
        # print(h1)
        for x in ach:
            
            p=x.month
            p1=x.year
            h2=int(p1+p)
            
            if(h1==h2):
                
                d={}
                d['user_id']=x.user_id
                d['achievement']=x.achievement_name
                ach1=UserDetails.objects.filter(user_id=x.user_id)
                for y in ach1:
                    d['name']=y.first_name+" "+y.last_name
                l.append(d)
        ans1=Notifications.objects.filter(user_id=user)
        ln=[]
        for x in ans1:
            d={}
            d['notification']=x.notification
            d['msg']=x.notification_message
            ln.append(d)
        users=UserDetails.objects.filter().exclude(user_id=user)
        l3=[]
        l2=[]
        skills=SkillList.objects.filter()
        for i in skills:
            ans=i.skill_name
            l2.append(ans)
       
        for i in users:
            ans=i.first_name+" "+i.last_name+"("+i.user_id+")"
            l3.append(ans)
        l11=json.dumps(l3)
        l12=json.dumps(l2)
        context={
            'users_names':l11,
            'skills':l12,
     
            'achievements':l,
            'userdetails':user_details,
              'notification':ln,
        }
        return render(request, 'felicitations.html',context)


def awards(request):
    if 'logged_in' in request.session:
        if request.method=='POST':
            award=int(request.POST['award'])
            user1=request.POST['name'][-7:]
            user2=user1[0:6]
            user=request.session['user_id']
            x=Nominations.objects.filter(award_id=award)
            
            c=0
            for i in x:
                c=i.no_of_nominations
            #ggfyhf
            x3=Nominate.objects.filter()
            x1=Nominate.objects.filter(award_id=award)
            hh=UserNominate.objects.filter(user_id=user)
            for x in hh:
                if x.award_id==award:
                    if x.nominated=='False':
                        print(1111)
                        if len(x1)==0:
                            Nominate.objects.create(award_id=award,user_id=user2,id=len(x3)+1,no_of_nominations=1)
                        else:
                            x2=Nominate.objects.filter(award_id=award,user_id=user2)
                            if len(x2)==0:
                                Nominate.objects.create(award_id=award,user_id=user2,id=len(x1)+1,no_of_nominations=1)
                            else:
                                Nominate.objects.filter(award_id=award,user_id=user2).update(no_of_nominations=len(x2)+1)
                        c+=1
                        Nominations.objects.filter(award_id=award).update(no_of_nominations=c)
                        UserNominate.objects.filter(user_id=user,award_id=award).update(nominated='True')
        user = request.session['user_id']
        date_now=datetime.now()
        date_present=date_now.strftime("%m/%d/%Y")
        user_details = UserDetails.objects.filter(user_id=user)
        ans1 = Notifications.objects.filter(user_id=user)
        nominations=Nominations.objects.filter()
        user=request.session['user_id']
        users=UserDetails.objects.filter().exclude(user_id=user)
        l=[]
        for x in nominations:
            d={}
            d['award_id']=x.award_id
            d['award_name']=x.award_name
            d['nominated']=x.no_of_nominations
            l.append(d)
        l1=[]
        for i in users:
            ans=i.first_name+" "+i.last_name+"("+i.user_id+")"
            l1.append(ans)
        l11=json.dumps(l1)
        ln = []
        for x in ans1:
            d = {}
            d['notification'] = x.notification
            d['msg'] = x.notification_message
            ln.append(d)
        users=UserDetails.objects.filter().exclude(user_id=user)
        l3=[]
        l2=[]
        skills=SkillList.objects.filter()
        for i in skills:
            ans=i.skill_name
            l2.append(ans)
       
        for i in users:
            ans=i.first_name+" "+i.last_name+"("+i.user_id+")"
            l3.append(ans)
        l11=json.dumps(l3)
        l12=json.dumps(l2)
        context={
            'users_names':l11,
            'skills':l12,
            'awards':l,
            'users_names':l11,
            'userdetails': user_details,
            'notification': ln,
        }
        return render(request, 'awards.html',context)


def talentassesments(request):
    if 'logged_in' in request.session:
        user=request.session['user_id']
        ans1=Notifications.objects.filter(user_id=user)
        user_details=UserDetails.objects.filter(user_id=user)
        topics=Topics.objects.filter()
        ln=[]
        for x in ans1:
            d={}
            d['notification']=x.notification
            d['msg']=x.notification_message
            ln.append(d)
        data={
            
            'userdetails':user_details,
              'notification':ln,
              'topics':topics
        }
        return render(request, 'talentassesments.html',data)


def rewards(request):
    if 'logged_in' in request.session:
        user = request.session['user_id']
        ans1 = Notifications.objects.filter(user_id=user)
        user_details = UserDetails.objects.filter(user_id=user)
        
        ln = []
        for x in ans1:
            d = {}
            d['notification'] = x.notification
            d['msg'] = x.notification_message
            ln.append(d)
        data = {

            'userdetails': user_details,
            'notification': ln,
            
        }
        return render(request, 'rewards.html',data)


def feedback(request):
    if 'logged_in' in request.session:
        user = request.session['user_id']
        ans1 = Notifications.objects.filter(user_id=user)
        user_details = UserDetails.objects.filter(user_id=user)

        ln = []
        for x in ans1:
            d = {}
            d['notification'] = x.notification
            d['msg'] = x.notification_message
            ln.append(d)
        data = {

            'userdetails': user_details,
            'notification': ln,

        }
        return render(request, 'feedback.html',data)

#yess
def goals(request):
    if 'logged_in' in request.session:
        user = request.session['user_id']
        ans1 = Notifications.objects.filter(user_id=user)
        user_details = UserDetails.objects.filter(user_id=user)

        ln = []
        for x in ans1:
            d = {}
            d['notification'] = x.notification
            d['msg'] = x.notification_message
            ln.append(d)
        goals=PersonalGoals.objects.filter(user_id=user)
        data = {

            'userdetails': user_details,
            'notification': ln,
            'goals':goals

        }
    
        return render(request, 'goals.html',data)

def queries(request):
    if 'logged_in' in request.session:

        if request.method=='POST':
            user = request.session['user_id']
            query_typ=request.POST['query_type']
            quer=request.POST['query']

            if query_typ!='0':
             
                p=PersonalQuery.objects.filter()
                PersonalQuery.objects.create(user_id=user,pquery_type=query_typ,pquery=quer,pquery_id=len(p)+1,id=len(p)+1) 
        user = request.session['user_id']
        ans1 = Notifications.objects.filter(user_id=user)
        user_details = UserDetails.objects.filter(user_id=user)

        ln = []
        for x in ans1:
            d = {}
            d['notification'] = x.notification
            d['msg'] = x.notification_message
            ln.append(d)
        data = {

            'userdetails': user_details,
            'notification': ln,

        }
        return render(request, 'queries.html',data)


def personaldm(request):
    return render(request, 'personaldm.html')


def techquery(request):
    return render(request, 'techquery.html')



def quiz(request):
    if 'logged_in' in request.session:
        user = request.session['user_id']
        user_details = UserDetails.objects.filter(user_id=user)
        if request.method=="GET":
            topic_id=request.GET['topic_id']
            data1=UserAnswers.objects.filter(user_id=user)
            for x in data1:
                print(x.topic_id)
                if str(x.topic_id)==str(topic_id):
                    print(10)
                    score=x.score
                    total=20
                    ans1 = Notifications.objects.filter(user_id=user)
                    percentage = (score/total)*100
                    ln = []
                    for x in ans1:
                        d = {}
                        d['notification'] = x.notification
                        d['msg'] = x.notification_message
                        ln.append(d)
                    topics = Topics.objects.filter(topic_id=request.session['topic_id'])
                    for t in topics:
                        topic = t.topic
                    data3 = {
                        'total': total,
                        'score': score,
                        'percentage': percentage,
                        'topic': topic,
                        'userdetails': user_details,
                        'notification': ln,

                    }
                    return render(request, 'result.html', data3)
            questions=Questions.objects.filter(topic_id=topic_id)
            request.session['topic_id'] = topic_id
        
            data = {

                'userdetails': user_details,
                'questions':questions,
            # 'notification': ln,
            
            }
            return render(request, 'quiz.html', data)
        else:
            topic_id = request.session['topic_id']
            topics = Topics.objects.filter(
                topic_id=request.session['topic_id'])
            data = Questions.objects.filter(
                topic_id=request.session['topic_id'])
            data1={
                'questions':data
            }
            score=0
            total=20
            for t in topics:
                topic=t.topic
            for f in data1['questions']:
                a=f.question
                x=0
                ans=request.POST[a]
                print(ans,f.answer)
                if ans==f.answer:
                    score+=1
                    x=1
            percentage=(score/total)*100
            UserAnswers.objects.create(topic_id=topic_id,user_id=user,score=score)
            ans1 = Notifications.objects.filter(user_id=user)
            ln = []
            for x in ans1:
                d = {}
                d['notification'] = x.notification
                d['msg'] = x.notification_message
                ln.append(d)
            data3={
                'total':total,
                'score':score,
                'percentage':percentage,
                'topic':topic,
                'userdetails': user_details,
                'notification': ln,
                
            }
            return render(request,'result.html', data3)


        


def projectfeed(request):
    if 'logged_in' in request.session:
        user = request.session['user_id']
        ans1 = Notifications.objects.filter(user_id=user)
        user_details = UserDetails.objects.filter(user_id=user)

        ln = []
        for x in ans1:
            d = {}
            d['notification'] = x.notification
            d['msg'] = x.notification_message
            ln.append(d)
        data = {

            'userdetails': user_details,
            'notification': ln,

        }
        return render(request, 'projectfeed.html',data)


def skillfeed(request):
    if 'logged_in' in request.session:
        user = request.session['user_id']
        ans1 = Notifications.objects.filter(user_id=user)
        user_details = UserDetails.objects.filter(user_id=user)

        ln = []
        for x in ans1:
            d = {}
            d['notification'] = x.notification
            d['msg'] = x.notification_message
            ln.append(d)
        users=UserDetails.objects.filter().exclude(user_id=user)
        l3=[]
        l2=[]
        skills=SkillList.objects.filter()
        for i in skills:
            ans=i.skill_name
            l2.append(ans)
       
        for i in users:
            ans=i.first_name+" "+i.last_name+"("+i.user_id+")"
            l3.append(ans)
        l11=json.dumps(l3)
        l12=json.dumps(l2)
        context={
            'users_names':l11,
            'skills':l12,

            'userdetails': user_details,
            'notification': ln,

        }
        return render(request, 'skillfeed.html',context)


def personal(request):
    if 'logged_in' in request.session:
        user = request.session['user_id']
        ans1 = Notifications.objects.filter(user_id=user)
        user_details = UserDetails.objects.filter(user_id=user)

        ln = []
        for x in ans1:
            d = {}
            d['notification'] = x.notification
            d['msg'] = x.notification_message
            ln.append(d)
        data = {

            'userdetails': user_details,
            'notification': ln,

        }
        return render(request, 'personal.html',data)

def postcommentmentions(request):
    if 'logged_in' in request.session:
        if request.method=='POST':
            user=request.session['user_id']
            postid=int(request.POST['post_id'])
            comment=request.POST['comment']
            x=PostReplies.objects.filter()
            PostReplies.objects.create(user_id=user,post_id=postid,reply=comment,id=len(x)+1)
            return redirect('/mentions/')

