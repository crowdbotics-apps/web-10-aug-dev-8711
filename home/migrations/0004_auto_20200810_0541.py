# Generated by Django 2.2.15 on 2020-08-10 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_auto_20200810_0538"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customtext", old_name="title11", new_name="titleChanged",
        ),
        migrations.RemoveField(model_name="homepage", name="body",),
        migrations.AddField(
            model_name="homepage", name="body123", field=models.TextField(blank=True),
        ),
    ]
