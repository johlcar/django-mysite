# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-19 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170519_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
