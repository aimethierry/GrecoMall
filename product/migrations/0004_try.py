# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-02 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Try',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='product/image')),
            ],
        ),
    ]
