# Generated by Django 4.2.15 on 2024-08-27 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0002_alter_profile_facebook_alter_profile_github_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='images'),
        ),
    ]
