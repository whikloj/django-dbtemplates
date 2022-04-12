# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django
from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dbtemplates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='Template',
            name='description',
            field=models.TextField(verbose_name='description', blank=True),
        ),
    ]
