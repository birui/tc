# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-12 03:36
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kz', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article_test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='\u6807\u9898')),
                ('content', ckeditor.fields.RichTextField(verbose_name='\u6b63\u6587')),
            ],
        ),
    ]
