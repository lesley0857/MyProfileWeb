# Generated by Django 4.2.15 on 2024-08-30 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0033_profile_linkedin_alter_profile_facebook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(max_length=400),
        ),
    ]
