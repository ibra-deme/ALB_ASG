# Generated by Django 4.1.2 on 2022-11-01 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compagnie', '0001_initial'),
        ('Vol', '0002_vol_trajet'),
    ]

    operations = [
        migrations.AddField(
            model_name='vol',
            name='compagnie',
            field=models.ManyToManyField(to='Compagnie.compagnie'),
        ),
    ]
