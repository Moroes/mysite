# Generated by Django 4.0.5 on 2022-09-07 09:34

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=True, populate_from='title', unique=True),
        ),
    ]