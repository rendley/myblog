# Generated by Django 2.0.5 on 2020-05-27 19:49

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_tag_status'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('custom_status_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
