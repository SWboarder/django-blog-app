# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-30 14:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160826_1104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='autor',
            new_name='author',
        ),
    ]
