# Generated by Django 4.2.4 on 2024-09-08 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_profile_full_name_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/user_images/default.jpg', upload_to='media/user_images/'),
        ),
    ]