# Generated by Django 4.0.5 on 2022-07-11 07:54

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True),
        ),
    ]
