# Generated by Django 5.0.7 on 2024-07-18 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("xuitter", "0006_profile_profile_img"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="profile_img",
            new_name="profile_image",
        ),
    ]