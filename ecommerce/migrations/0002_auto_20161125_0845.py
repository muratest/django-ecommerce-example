# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, upload_to='images/', verbose_name='商品画像'),
        ),
    ]
