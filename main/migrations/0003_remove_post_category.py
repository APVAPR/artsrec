# Generated by Django 3.2.9 on 2021-11-20 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_user_id_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
