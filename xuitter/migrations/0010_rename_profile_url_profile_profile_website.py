# Generated by Django 5.0.7 on 2024-07-19 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("xuitter", "0009_profile_profile_bio_profile_profile_url"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="profile_url",
            new_name="profile_website",
        ),
    ]