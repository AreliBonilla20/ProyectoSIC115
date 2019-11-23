# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-11-19 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Planilla', '0002_auto_20191113_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='salario',
            name='renta',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Retencio de renta'),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='gerencia',
            field=models.CharField(blank=True, choices=[('ti', 'TI'), ('ventas', 'Ventas'), ('contabilidad', 'Contabilidad'), ('operaciones', 'Operaciones')], max_length=100, null=True),
        ),
    ]