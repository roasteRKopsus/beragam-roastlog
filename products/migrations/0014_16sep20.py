# Generated by Django 3.0.8 on 2020-09-16 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_16sep20'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengambilangreenbean',
            name='beans_name',
            field=models.ForeignKey(limit_choices_to={'show_this': True}, on_delete=django.db.models.deletion.CASCADE, to='products.BeansGudang'),
        ),
    ]
#done updated 16 sep 20