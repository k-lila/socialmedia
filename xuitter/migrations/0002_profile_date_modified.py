# Generated by Django 5.0.7 on 2024-07-16 23:11

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("xuitter", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="date_modified",
            field=models.DateTimeField(
                auto_now=True, verbose_name=django.contrib.auth.models.User
            ),
        ),
    ]