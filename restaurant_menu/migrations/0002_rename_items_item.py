# Generated by Django 5.1.1 on 2024-09-04 19:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_menu', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Items',
            new_name='Item',
        ),
    ]
