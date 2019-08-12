# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-08-12 02:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_formdata_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdata',
            name='template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='form_manager.Template'),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='form_manager.UserProfile'),
        ),
    ]