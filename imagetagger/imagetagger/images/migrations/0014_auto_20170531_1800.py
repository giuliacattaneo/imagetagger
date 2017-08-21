# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0013_auto_20170523_0301'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imageset',
            options={'permissions': (('edit_set', 'Edit set'), ('delete_set', 'Delete set'), ('edit_annotation', 'Edit annotations in the set'), ('delete_annotion', 'Delete annotations in the set'), ('annotate', 'Create annotations in the set'), ('read', 'Read and download annotations and images'), ('create_export', 'Create export files of the set'), ('delete_export', 'Delete export files of the set'))},
        ),
        migrations.AlterField(
            model_name='imageset',
            name='path',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]