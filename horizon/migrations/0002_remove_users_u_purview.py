# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-04 16:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('horizon', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='u_purview',
        ),
    ]
