# Generated by Django 3.0.6 on 2020-05-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gideon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
