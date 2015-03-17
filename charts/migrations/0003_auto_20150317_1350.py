# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0002_auto_20150316_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='city',
            field=models.CharField(unique=True, max_length=30),
            preserve_default=True,
        ),
    ]
