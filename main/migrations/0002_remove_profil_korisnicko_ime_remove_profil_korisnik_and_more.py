# Generated by Django 4.0.1 on 2022-02-20 10:57

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='korisnicko_ime',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='korisnik',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='slika_profil',
        ),
        migrations.AddField(
            model_name='profil',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.user_directory_path, verbose_name='Picture'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='bio',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]
