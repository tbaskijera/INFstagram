# Generated by Django 4.0.1 on 2022-02-22 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='c',
            field=models.IntegerField(default=1),
        ),
    ]
