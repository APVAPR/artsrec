# Generated by Django 3.2.9 on 2021-11-22 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['post'], 'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
    ]
