# Generated by Django 5.1.3 on 2024-12-15 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_socialmediauser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SocialMediaUser',
        ),
    ]