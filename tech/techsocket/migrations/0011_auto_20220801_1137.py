# Generated by Django 2.1 on 2022-08-01 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techsocket', '0010_awards_nominate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nominations',
            name='end_month',
        ),
        migrations.RemoveField(
            model_name='nominations',
            name='start_month',
        ),
    ]