# Generated by Django 4.2.15 on 2024-08-30 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0025_remove_clients_user_clients_seller_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='seller_profile',
            field=models.ManyToManyField(blank=True, related_name='clients', to='profileapp.profile'),
        ),
    ]
