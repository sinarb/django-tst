# Generated by Django 4.1.5 on 2023-02-04 15:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_todo_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='Note',
        ),
    ]
