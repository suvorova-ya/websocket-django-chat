# Generated by Django 4.1.3 on 2022-12-25 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_room_online'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='current_users',
            new_name='user',
        ),
    ]
