# Generated by Django 2.1 on 2022-07-25 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('techsocket', '0002_delete_ex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]