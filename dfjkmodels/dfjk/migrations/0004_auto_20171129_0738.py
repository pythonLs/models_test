# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfjk', '0003_device_depot_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operate_account', models.CharField(max_length=20, verbose_name='\u64cd\u4f5c\u8d26\u53f7')),
            ],
            options={
                'verbose_name': '\u51fa\u5e93\u8bb0\u5f55',
                'verbose_name_plural': '\u51fa\u5e93\u8bb0\u5f55',
            },
        ),
        migrations.AlterField(
            model_name='device',
            name='depot_name',
            field=models.CharField(help_text='\u663e\u793a\u5728\u4e0b\u65b9\u5417', max_length=20, null=True, verbose_name='\u8bbe\u5907\u5e93\u623f\u540d\u79f0', blank=True),
        ),
        migrations.AddField(
            model_name='outrecord',
            name='device',
            field=models.ManyToManyField(to='dfjk.Device', verbose_name='\u8bbe\u5907\u4fe1\u606f'),
        ),
    ]
