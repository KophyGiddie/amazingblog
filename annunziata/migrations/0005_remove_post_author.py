# Generated by Django 3.0.6 on 2020-05-13 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annunziata', '0004_auto_20200513_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]