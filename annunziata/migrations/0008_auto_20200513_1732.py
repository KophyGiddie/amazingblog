# Generated by Django 3.0.6 on 2020-05-13 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annunziata', '0007_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='content',
        ),
    ]
