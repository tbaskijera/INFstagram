# Generated by Django 4.0.1 on 2022-02-21 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_objava_profil_objava'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='komentar',
            name='lajk_komentar',
        ),
        migrations.AddField(
            model_name='komentar',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='komentar',
            name='body',
            field=models.TextField(default='komentar'),
        ),
    ]
