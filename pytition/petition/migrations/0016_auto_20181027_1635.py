# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-27 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0015_organization_default_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='pytitionuser',
            name='default_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='petition.PetitionTemplate', verbose_name='Default petition template'),
        ),
        migrations.AddField(
            model_name='pytitionuser',
            name='petition_templates',
            field=models.ManyToManyField(blank=True, to='petition.PetitionTemplate', verbose_name='Petition templates'),
        ),
    ]
