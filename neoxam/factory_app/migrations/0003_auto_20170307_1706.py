# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-07 17:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('factory_app', '0002_auto_20170303_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.IntegerField(choices=[(0, 'Normal'), (-10, 'High')], default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='compiler',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='factory_app.Compiler'),
        ),
        migrations.AlterField(
            model_name='task',
            name='procedure_revision',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='factory_app.ProcedureRevision'),
        ),
    ]