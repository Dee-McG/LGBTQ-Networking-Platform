# Generated by Django 4.2.2 on 2023-06-18 23:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mentors", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mentorrequest",
            name="content",
        ),
    ]
