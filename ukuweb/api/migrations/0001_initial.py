# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-08-16 03:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FormData",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.CharField(blank=True, max_length=500)),
                ("coordinates", models.CharField(max_length=100, null=True)),
                ("data", models.TextField()),
                ("access_date", models.DateField(blank=True, null=True)),
                ("created_date", models.DateField(blank=True, null=True)),
                ("send_date", models.DateField(blank=True, null=True)),
                ("include_gps", models.BooleanField(default=False)),
                ("reason", models.CharField(blank=True, null=True, max_length=500)),
            ],
        )
    ]
