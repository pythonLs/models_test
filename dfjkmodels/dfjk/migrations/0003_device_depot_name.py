# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfjk', '0002_auto_20171128_0320'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='depot_name',
            field=models.CharField(max_length=20, verbose_name='\u8bbe\u5907\u5e93\u623f\u540d\u79f0', blank=True),
        ),
    ]
