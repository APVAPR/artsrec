# Generated by Django 3.2.9 on 2021-11-21 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211120_1659'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['date_create'], 'verbose_name': 'Рекомендация', 'verbose_name_plural': 'Рекомендации'},
        ),
    ]
