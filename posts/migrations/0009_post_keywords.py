# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 22:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_post_meta_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='keywords',
            field=models.CharField(default=datetime.datetime(2016, 2, 23, 22, 7, 2, 903969, tzinfo=utc), max_length=120),
            preserve_default=False,
        ),
    ]
