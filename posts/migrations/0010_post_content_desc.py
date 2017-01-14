# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 10:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_post_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_desc',
            field=models.TextField(default=datetime.datetime(2016, 2, 24, 10, 32, 3, 121611, tzinfo=utc)),
            preserve_default=False,
        ),
    ]