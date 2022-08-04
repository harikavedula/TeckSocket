"""tech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from techsocket import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    path('logout/',views.logout,name="logout"),
    path('index/', views.index, name='index'), 
    path('mentions/', views.mentions, name="mentions"), 
    path('teamoverview/', views.teamoverview, name="teamoverview"),
    path('people/', views.people, name="people"),
    path('incentives/', views.incentives, name="incentives"),
    path('felicitations/', views.felicitations, name="felicitations"),
    path('awards/', views.awards, name="awards"),
    path('talentassesments/', views.talentassesments, name="talentassesments"),
    path('goals/', views.goals, name="goals"),
    path('rewards/', views.rewards, name="rewards"),
    path('feedback/', views.feedback, name="feedback"),
    path('queries/', views.queries, name="queries"),
    path('personaldm/', views.personaldm, name="personaldm"),
    path('techquery/', views.techquery, name="techquery"),
    path('sendrecognition/',views.sendrecognition,name="sendrecognition"),
    path('quiz/', views.quiz, name="quiz"),
    path('projectfeed/', views.projectfeed, name="projectfeed"),
    path('skillfeed/', views.skillfeed, name="skillfeed"),
    path('personal/', views.personal, name="personal"),
]