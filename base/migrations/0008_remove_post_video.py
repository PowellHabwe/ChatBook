# Generated by Django 4.0.5 on 2022-08-22 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_post_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
    ]
