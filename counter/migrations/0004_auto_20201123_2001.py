# Generated by Django 3.1.3 on 2020-11-23 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0003_auto_20201123_1959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search',
            old_name='request',
            new_name='link',
        ),
    ]
