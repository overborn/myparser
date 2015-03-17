# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0003_auto_20150317_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='city',
            field=models.CharField(max_length=30, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='region',
            field=models.CharField(max_length=30, db_index=True),
            preserve_default=True,
        ),
    ]
