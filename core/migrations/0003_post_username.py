# Generated by Django 4.2.4 on 2023-09-24 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
