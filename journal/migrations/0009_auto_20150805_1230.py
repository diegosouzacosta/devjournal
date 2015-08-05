# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0008_auto_20150805_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='email',
            field=models.CharField(max_length=150, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manager',
            name='email',
            field=models.CharField(max_length=150, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='developer',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='manager',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
