# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-20 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170519_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
