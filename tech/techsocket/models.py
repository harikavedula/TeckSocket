from operator import truth
from re import U
from django.db import models
from django.db.models import CASCADE
import jsonfield

class User(models.Model):
    user_id=models.CharField(max_length=8,primary_key=True)
    email=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=20)

class UserDetails(models.Model):
    picture=models.TextField()
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    user_id=models.ForeignKey(to=User,db_column='user_id',on_delete=CASCADE)
    address=models.TextField()
    phone_no=models.CharField(max_length=13)
    educational_qualifications=models.TextField()
    designation=models.CharField(max_length=50)
    join_date=models.CharField(max_length=20)
    join_year=models.TextField(default=0)
    join_month=models.TextField(default=0)
    join_date_no=models.TextField(default=0)
    social_media=models.TextField(default=0)

class Birthdays(models.Model):
    birth_day=models.CharField(max_length=5)
    birth_month=models.CharField(max_length=20)
    user_id=models.ForeignKey(to=User,db_column='user_id',on_delete=CASCADE)

class Posts(models.Model):
    post=models.TextField()
    post_id=models.IntegerField(primary_key=True)
    mentions=models.TextField()

class PostReplies(models.Model):
    post_id=models.ForeignKey(to=Posts,db_column='post_id',on_delete=CASCADE)
    user_id=models.ForeignKey(to=User,db_column='user_id',on_delete=CASCADE)
    reply=models.TextField()
    
class PostReactions(models.Model):
    user_id=models.ForeignKey(to=User,db_column='user_id',on_delete=CASCADE)
    reaction=models.TextField()
    post_id=models.ForeignKey(to=Posts,db_column='post_id',on_delete=CASCADE)

class EthicalValues(models.Model):
    ethical_value_name=models.TextField()
    ethical_value_id=models.CharField(max_length=10,primary_key=True)


class SkillList(models.Model):
    skill_id=models.CharField(max_length=10)
    skill_name=models.CharField(max_length=50)

class Notifications(models.Model):
    notification_id=models.IntegerField()
    notification_message=models.TextField()
    user_id=models.ForeignKey(to=User,db_column='user_id',on_delete=CASCADE)
    truth_value=models.BooleanField()

class Team(models.Model):
    team_name=models.TextField()
    team_id=models.IntegerField()
    user_id=models.ForeignKey(to=User,db_column='user_id',on_delete=CASCADE)
    members_list=models.TextField()

class Nominations(models.Model):
    user_id=models.ForeignKey(to=User,db_column='user_id',on_delete=CASCADE)
    award_name=models.TextField()
    no_of_nominations=models.IntegerField()
    start_date=models.TextField()
    end_date=models.TextField()

class TeamGoals(models.Model):
    team_id=models.ForeignKey(to=Team,db_column='team_id',on_delete=CASCADE)
    goal=models.TextField()
    deadline=models.TextField()

class PersonalGoals(models.Model):
    user_id=models.ForeignKey(to=User,db_column='user_id',on_delete=CASCADE)
    goal=models.TextField()
    deadline=models.TextField()

class Query(models.Model):
    query_id=models.IntegerField(primary_key=True)
    query=models.TextField()
    hastags=models.TextField()
    user_id=models.ForeignKey(to=User,db_column='user_id',on_delete=CASCADE)

class QueryReplies(models.Model):
    query_id=models.ForeignKey(to=Query,db_column='query_id',on_delete=CASCADE)
    reply=models.TextField()
    user_id=models.ForeignKey(to=User,db_column='user_id',on_delete=CASCADE)

class Dm(models.Model):
    rec_user_id=models.ForeignKey(to=User,db_column='user_id',on_delete=CASCADE)
    send_user_id=models.CharField(max_length=8)
    messages=models.TextField()
    date=models.TextField()
    time=models.TextField()
    documents=models.TextField()
    photos=models.TextField()

class Greetings(models.Model):
    greeting_id=models.IntegerField()
    greeting_name=models.TextField()
    posted_date=models.TextField()
    reactions=models.TextField()
    

class Feedback(models.Model):
    rec_user_id=models.ForeignKey(to=User,db_column='user_id',on_delete=CASCADE)
    send_user_id=models.CharField(max_length=8)
    feedback_content=models.TextField()


