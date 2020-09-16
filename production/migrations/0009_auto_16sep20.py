# Generated by Django 3.0.8 on 2020-09-16 13:24

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0008_auto_15sep20'),
    ]

    operations = [
        migrations.AddField(
            model_name='kejadian',
            name='tingkat_urgensi',
            field=models.CharField(choices=[('B', 'Biasa'), ('M', 'Medium'), ('P', 'Parah'), ('R', 'Rutinitas')], default='B', max_length=1),
        ),
    ]