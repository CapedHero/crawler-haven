# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 14:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webcrawler',
            old_name='web_crawler',
            new_name='script',
        ),
    ]
