# Generated by Django 4.1.2 on 2022-10-21 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('star_wars_universe', '0002_rename_planet_character_planet_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='birthdate',
        ),
    ]