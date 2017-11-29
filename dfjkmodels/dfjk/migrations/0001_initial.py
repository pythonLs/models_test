# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BindRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('car_identification_num', models.CharField(help_text='\u8f66\u8f86\u8bc6\u522b\u7801', max_length=30, verbose_name='\u8f66\u8f86\u8bc6\u522b\u7801')),
                ('operate_account', models.CharField(max_length=20, verbose_name='\u64cd\u4f5c\u8d26\u53f7')),
                ('operation_phone', models.CharField(max_length=20, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('operation_remarks', models.CharField(default='', max_length=20, verbose_name='\u64cd\u4f5c\u5907\u6ce8')),
                ('binding_time', models.DateTimeField(verbose_name='\u7ed1\u5b9a\u65f6\u95f4', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_id', models.CharField(help_text='\u8bbe\u5907id', unique=True, max_length=20, verbose_name='\u8bbe\u5907ID')),
                ('sim_id', models.CharField(unique=True, max_length=20, verbose_name='\u8bbe\u5907SIM ID')),
                ('depot_name', models.CharField(default='', max_length=20, verbose_name='\u8bbe\u5907\u5e93\u623f\u540d\u79f0')),
                ('destroy_time', models.DateTimeField(verbose_name='\u9500\u6bc1\u65f6\u95f4', blank=True)),
                ('remove_binding_time', models.DateTimeField(verbose_name='\u89e3\u7ed1\u65f6\u95f4', blank=True)),
                ('binding_time', models.DateTimeField(verbose_name='\u7ed1\u5b9a\u65f6\u95f4', blank=True)),
                ('sell_time', models.DateTimeField(verbose_name='\u51fa\u8ba9\u65f6\u95f4(\u6240\u5c5e\u6743\u53d8\u66f4\u4e3a\u7ecf\u9500\u5546\u7684\u65f6\u95f4\uff09', blank=True)),
                ('send_time', models.DateTimeField(verbose_name='\u5bc4\u56de\u65f6\u95f4', blank=True)),
                ('device_in_time', models.DateTimeField(auto_now_add=True, verbose_name='\u5165\u5e93\u65f6\u95f4')),
                ('device_out_time', models.DateTimeField(verbose_name='\u51fa\u5e93\u65f6\u95f4', blank=True)),
                ('device_position', models.CharField(default='all_warehouse', max_length=20, verbose_name='\u6240\u5728\u4f4d\u7f6e', choices=[('on_line', '\u5728\u9014'), ('all_depot', '\u603b\u5e93'), ('dealer_depot', '\u7ecf\u9500\u5546\u5e93\u5b58'), ('client_depot', '\u5ba2\u6237\u5e93\u5b58')])),
                ('device_status', models.CharField(default='unbinding', max_length=10, verbose_name='\u7ed1\u5b9a\u72b6\u6001', choices=[('binding', '\u5df2\u7ed1\u5b9a'), ('unbinding', '\u672a\u7ed1\u5b9a')])),
                ('device_ownership', models.CharField(default='cwjh', max_length=20, verbose_name='\u6240\u5c5e\u6743\u5f52\u5c5e', choices=[('cwjh', '\u4f20\u4e3a\u4f73\u8bdd'), ('dealer', '\u7ecf\u9500\u5546'), ('big_client', '\u5927\u5ba2\u6237')])),
                ('device_remarks', models.CharField(default='', max_length=20, verbose_name='\u8bbe\u5907\u5907\u6ce8')),
                ('is_new_device', models.BooleanField(default=True, verbose_name='\u662f\u5426\u4e3a\u65b0\u8bbe\u5907')),
            ],
        ),
        migrations.CreateModel(
            name='EnterRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operate_account', models.CharField(max_length=20, verbose_name='\u64cd\u4f5c\u8d26\u53f7')),
                ('operation_phone', models.CharField(max_length=20, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('operation_remarks', models.CharField(default='', max_length=20, verbose_name='\u64cd\u4f5c\u5907\u6ce8')),
                ('device_in_time', models.DateTimeField(auto_now_add=True, verbose_name='\u5165\u5e93\u65f6\u95f4')),
                ('device_status', models.CharField(default='unbinding', max_length=10, verbose_name='\u7ed1\u5b9a\u72b6\u6001', choices=[('binding', '\u5df2\u7ed1\u5b9a'), ('unbinding', '\u672a\u7ed1\u5b9a')])),
                ('device', models.ManyToManyField(to='dfjk.Device')),
            ],
        ),
        migrations.CreateModel(
            name='OutRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operate_account', models.CharField(max_length=20, verbose_name='\u64cd\u4f5c\u8d26\u53f7')),
                ('operation_phone', models.CharField(max_length=20, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('operation_remarks', models.CharField(default='', max_length=20, verbose_name='\u64cd\u4f5c\u5907\u6ce8')),
                ('device_out_time', models.DateTimeField(verbose_name='\u51fa\u5e93\u65f6\u95f4', blank=True)),
                ('device', models.ManyToManyField(to='dfjk.Device')),
            ],
        ),
        migrations.CreateModel(
            name='RemoveBindingRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('car_identification_num', models.CharField(help_text='\u8f66\u8f86\u8bc6\u522b\u7801', max_length=30, verbose_name='\u8f66\u8f86\u8bc6\u522b\u7801')),
                ('operate_account', models.CharField(max_length=20, verbose_name='\u64cd\u4f5c\u8d26\u53f7')),
                ('operation_phone', models.CharField(max_length=20, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('operation_remarks', models.CharField(default='', max_length=20, verbose_name='\u64cd\u4f5c\u5907\u6ce8')),
                ('device', models.ManyToManyField(to='dfjk.Device')),
            ],
            options={
                'verbose_name': '\u89e3\u7ed1\u8bb0\u5f55',
                'verbose_name_plural': '\u89e3\u7ed1\u8bb0\u5f55',
            },
        ),
        migrations.AddField(
            model_name='bindrecord',
            name='device',
            field=models.ManyToManyField(to='dfjk.Device'),
        ),
    ]
