from django.db import models

class Ex(models.Model):
    name=models.CharField(max_length=30)