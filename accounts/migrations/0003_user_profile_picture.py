# Generated by Django 4.2.11 on 2024-03-09 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_first_name_user_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics/', verbose_name='Profile Picture'),
        ),
    ]
