# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-12 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folha', '0002_auto_20180412_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='Grau_Instrucao',
            field=models.CharField(choices=[('Analfabeto', 'Analfabeto'), ('Ensino Fundamental Incompleto', 'Ensino Fundamental Incompleto'), ('Ensino Fundamental Completo', 'Ensino Fundamental Completo'), ('Ensino Médio Incompleto', 'Ensino Médio Incompleto'), ('Ensino Médio Completo', 'Ensino Médio Completo'), ('Superior completo (ou Graduação)', 'Superior completo (ou Graduação)'), ('Pós-Graduação', 'Pós-Graduação'), ('Mestrado', 'Mestrado'), ('Doutorado', 'Doutorado'), ('PHD', 'PHD')], help_text='Escolaridade do colaborador', max_length=50),
        ),
    ]