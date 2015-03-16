# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('value', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
