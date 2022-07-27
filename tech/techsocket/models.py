from xmlrpc.client import Boolean
from django.db import models

class User(models.Model):
    user_id=models.CharField(max_length=8)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=20)

class UserDetails(models.Model):
    picture=models.TextField()
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    user_id=models.CharField(max_length=8)
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
    user_id=models.CharField(max_length=8)

class Posts(models.Model):
    user_id=models.CharField(max_length=8)
    post=models.TextField()
    post_id=models.IntegerField()
    mentions=models.TextField()

class PostReplies(models.Model):
    post_id=models.IntegerField()
    user_id=models.CharField(max_length=8)
    reply=models.TextField()
    
class PostReactions(models.Model):
    user_id=models.CharField(max_length=8)
    reaction=models.TextField()
    post_id=models.IntegerField()

class EthicalValues(models.Model):
    ethical_value_name=models.TextField()
    ethical_value_id=models.CharField(max_length=10)


class SkillList(models.Model):
    skill_id=models.CharField(max_length=10)
    skill_name=models.CharField(max_length=50)

class Notifications(models.Model):
    notification_id=models.IntegerField()
    notification_message=models.TextField()
    user_id=models.CharField(max_length=8)
    truth_value=models.TextField()

class Team(models.Model):
    team_name=models.TextField()
    team_id=models.IntegerField()
    user_id=models.CharField(max_length=8)
    members_list=models.TextField()

class Nominations(models.Model):
    user_id=models.CharField(max_length=8)
    award_name=models.TextField()
    no_of_nominations=models.IntegerField()
    start_date=models.TextField()
    end_date=models.TextField()

class TeamGoals(models.Model):
    team_id=models.IntegerField()
    goal=models.TextField()
    deadline=models.TextField()

class PersonalGoals(models.Model):
    user_id=models.CharField(max_length=8)
    goal=models.TextField()
    deadline=models.TextField()

class Query(models.Model):
    query_id=models.IntegerField()
    query=models.TextField()
    hastags=models.TextField()
    user_id=models.CharField(max_length=8)

class QueryReplies(models.Model):
    query_id=models.IntegerField()
    reply=models.TextField()
    user_id=models.CharField(max_length=8)

class Dm(models.Model):
    rec_user_id=models.CharField(max_length=8)
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
    rec_user_id=models.CharField(max_length=8)
    send_user_id=models.CharField(max_length=8)
    feedback_content=models.TextField()

class PostSeen(models.Model):
    post_id=models.TextField()
    user_id=models.CharField(max_length=30)
    seen=models.TextField()


