# Generated by Django 4.2.15 on 2024-08-29 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0013_alter_projects_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_link',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='website_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
