# Generated by Django 4.0.1 on 2022-01-19 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Video', '0002_video_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='writer',
        ),
    ]