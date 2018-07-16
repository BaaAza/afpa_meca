# Generated by Django 2.0.5 on 2018-07-16 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicule',
            name='type_vehicule',
        ),
        migrations.AddField(
            model_name='vehicule',
            name='Type_vehicule',
            field=models.CharField(choices=[('voiture', 'Voiture'), ('moto', 'Moto'), ('velo', 'Velo')], default=('voiture', 'Voiture'), max_length=10),
        ),
    ]