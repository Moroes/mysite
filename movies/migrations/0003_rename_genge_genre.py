# Generated by Django 4.0.5 on 2022-06-08 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_rating_movie'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Genge',
            new_name='Genre',
        ),
    ]
