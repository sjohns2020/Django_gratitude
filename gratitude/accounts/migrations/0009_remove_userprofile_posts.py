# Generated by Django 4.1.7 on 2023-03-29 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0008_alter_userprofile_posts"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="posts",
        ),
    ]
