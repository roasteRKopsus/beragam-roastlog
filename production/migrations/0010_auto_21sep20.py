# Generated by Django 3.0.8 on 2020-09-21 07:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_21sep20'),
        ('production', '0009_auto_16sep20'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barangkeluar',
            name='tanggal_dan_jam',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 21, 14, 32, 53, 936766)),
        ),
        migrations.AlterField(
            model_name='komposisibean',
            name='tanggal_pembuatan_komposisi',
            field=models.DateField(default=datetime.date(2020, 9, 21)),
        ),
        migrations.AlterField(
            model_name='packforminput',
            name='tanggal_dan_jam',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 21, 14, 32, 53, 936766)),
        ),
        migrations.AlterField(
            model_name='productiondiv',
            name='production_date',
            field=models.ForeignKey(limit_choices_to={'production_date': datetime.date(2020, 9, 21)}, on_delete=django.db.models.deletion.CASCADE, to='production.BlendReport'),
        ),
        migrations.AlterField(
            model_name='productiondiv',
            name='roast_date',
            field=models.DateField(default=datetime.date(2020, 9, 21)),
        ),
        migrations.AlterField(
            model_name='productiondiv',
            name='roasted_material',
            field=models.ManyToManyField(to='products.Roaster'),
        ),
    ]