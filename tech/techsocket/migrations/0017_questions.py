# Generated by Django 2.1 on 2022-08-05 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techsocket', '0016_topics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_id', models.IntegerField()),
                ('question_no', models.IntegerField()),
                ('question', models.TextField()),
                ('option_1', models.CharField(max_length=200)),
                ('option_2', models.CharField(max_length=200)),
                ('option_3', models.CharField(max_length=200)),
                ('option_4', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=8)),
            ],
        ),
    ]