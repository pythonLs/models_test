# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfjk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bindrecord',
            name='device',
        ),
        migrations.RemoveField(
            model_name='enterrecord',
            name='device',
        ),
        migrations.RemoveField(
            model_name='outrecord',
            name='device',
        ),
        migrations.RemoveField(
            model_name='removebindingrecord',
            name='device',
        ),
        migrations.RemoveField(
            model_name='device',
            name='binding_time',
        ),
        migrations.RemoveField(
            model_name='device',
            name='depot_name',
        ),
        migrations.RemoveField(
            model_name='device',
            name='device_in_time',
        ),
        migrations.RemoveField(
            model_name='device',
            name='device_out_time',
        ),
        migrations.RemoveField(
            model_name='device',
            name='device_ownership',
        ),
        migrations.RemoveField(
            model_name='device',
            name='device_position',
        ),
        migrations.RemoveField(
            model_name='device',
            name='device_remarks',
        ),
        migrations.RemoveField(
            model_name='device',
            name='device_status',
        ),
        migrations.RemoveField(
            model_name='device',
            name='is_new_device',
        ),
        migrations.RemoveField(
            model_name='device',
            name='remove_binding_time',
        ),
        migrations.RemoveField(
            model_name='device',
            name='sell_time',
        ),
        migrations.RemoveField(
            model_name='device',
            name='send_time',
        ),
        migrations.RemoveField(
            model_name='device',
            name='sim_id',
        ),
        migrations.AlterField(
            model_name='device',
            name='destroy_time',
            field=models.DateTimeField(null=True, verbose_name='\u9500\u6bc1\u65f6\u95f4', blank=True),
        ),
        migrations.DeleteModel(
            name='BindRecord',
        ),
        migrations.DeleteModel(
            name='EnterRecord',
        ),
        migrations.DeleteModel(
            name='OutRecord',
        ),
        migrations.DeleteModel(
            name='RemoveBindingRecord',
        ),
    ]
