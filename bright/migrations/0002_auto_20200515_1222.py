# Generated by Django 3.0.6 on 2020-05-15 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bright', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='modified_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
