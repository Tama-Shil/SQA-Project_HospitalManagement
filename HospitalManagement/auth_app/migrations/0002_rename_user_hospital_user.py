# Generated by Django 5.0.1 on 2024-02-25 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Hospital_User',
        ),
    ]
