# Generated by Django 4.0.1 on 2022-02-21 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_objava_lajk_objava_alter_objava_profil_objava_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objava',
            name='profil_objava',
        ),
    ]
