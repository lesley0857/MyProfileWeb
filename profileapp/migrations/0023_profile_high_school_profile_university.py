# Generated by Django 4.2.15 on 2024-08-29 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0022_profile_herofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='high_school',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='university',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
