# Generated by Django 4.0.5 on 2022-07-06 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_post_date_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now_add=True, db_index=True, verbose_name='Дата добавления'),
        ),
    ]
