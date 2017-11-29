# coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Device(models.Model):
    """
    监控设备状态信息
    """
    DEVICE_POSSITION_CHOICES = (
        ('on_line', u'在途'),
        ('all_depot', u'总库'),
        ('dealer_depot', u'经销商库存'),
        ('client_depot', u'客户库存')
    )
    DEVICE_STATUS_CHOICES = (
        ('binding', u'已绑定'),
        ('unbinding', u'未绑定'),
    )
    DEVICE_BELONGTO_CHOICES = (
        ('cwjh', u'传为佳话'),
        ('dealer', u'经销商'),
        ('big_client', u'大客户'),
    )

    OBD_TYPE_META = (
        (),
    )
    device_id = models.CharField(
        u'设备ID',
        max_length=20,
        unique=True,
        help_text=u'设备id'
    )
#     sim_id = models.CharField(
#         u'设备SIM ID',
#         max_length=20,
#         unique=True,
#     )
    depot_name = models.CharField(
        u'设备库房名称',
        blank=True,
        max_length=20,
        null=True,
        # default='',
        help_text='显示在下方吗',
    )
    destroy_time = models.DateTimeField(
        u'销毁时间',
        blank=True,
        null=True,
    )
#     remove_binding_time = models.DateTimeField(
#         u'解绑时间',
#         blank=True,
#     )
#     binding_time = models.DateTimeField(
#         u'绑定时间',
#         blank=True,
#     )
#     sell_time = models.DateTimeField(
#         u'出让时间(所属权变更为经销商的时间）',
#         blank=True,
#     )
#     send_time = models.DateTimeField(
#         u'寄回时间',
#         blank=True,
#     )
#     device_in_time = models.DateTimeField(
#         u'入库时间',
#         auto_now_add=True,
#     )
#     device_out_time = models.DateTimeField(
#         u'出库时间',
#         blank=True,
#     )
#     device_position = models.CharField(
#         u'所在位置',
#         default='all_warehouse',
#         max_length=20,
#         choices=DEVICE_POSSITION_CHOICES,
#     )
#     device_status = models.CharField(
#         u'绑定状态',
#         default='unbinding',
#         max_length=10,
#         choices=DEVICE_STATUS_CHOICES,
#     )
#     device_ownership = models.CharField(
#         u'所属权归属',
#         default='cwjh',
#         max_length=20,
#         choices=DEVICE_BELONGTO_CHOICES,
#     )
#     device_remarks = models.CharField(
#         u'设备备注',
#         default='',
#         max_length=20,
#     )
#     is_new_device = models.BooleanField(
#         u'是否为新设备',
#         default=True,
#     )
#
#     def __unicode__(self):
#         return self.device_id
#
#
#
# class EnterRecord(models.Model):
#     """
#     入库记录
#     """
#     DEVICE_STATUS_CHOICES = (
#         ('binding', u'已绑定'),
#         ('unbinding', u'未绑定'),
#     )
#     operate_account = models.CharField(
#         u'操作账号',
#         max_length=20,
#     )
#     operation_phone = models.CharField(
#         u'联系电话',
#         max_length=20,
#     )
#     operation_remarks = models.CharField(
#         u'操作备注',
#         default='',
#         max_length=20,
#     )
#     device_in_time = models.DateTimeField(
#         u'入库时间',
#         auto_now_add=True,
#     )
#     device_status = models.CharField(
#         u'绑定状态',
#         default='unbinding',
#         max_length=10,
#         choices=DEVICE_STATUS_CHOICES,
#     )
#     device = models.ManyToManyField(
#         'Device',
#     )
#
#     def __unicode__(self):
#         return self.operate_account
#
#
class OutRecord(models.Model):
    """
    出库记录
    """
    operate_account = models.CharField(
        u'操作账号',
        max_length=20,
    )
#     operation_phone = models.CharField(
#         u'联系电话',
#         max_length=20,
#     )
#     operation_remarks = models.CharField(
#         u'操作备注',
#         default='',
#         max_length=20,
#     )
#     device_out_time = models.DateTimeField(
#         u'出库时间',
#         blank=True,
#     )
    device = models.ManyToManyField(
        'Device',
        verbose_name=u'设备信息'
    )

    def __unicode__(self):
        return self.operate_account

    class Meta:
        verbose_name = u'出库记录'
        verbose_name_plural = verbose_name
#
#
# class BindRecord(models.Model):
#     """
#     绑定记录
#     """
#     car_identification_num = models.CharField(
#         u'车辆识别码',
#         max_length=30,
#         help_text=u'车辆识别码',
#     )
#     operate_account = models.CharField(
#         u'操作账号',
#         max_length=20,
#     )
#     operation_phone = models.CharField(
#         u'联系电话',
#         max_length=20,
#     )
#     operation_remarks = models.CharField(
#         u'操作备注',
#         default='',
#         max_length=20,
#     )
#     binding_time = models.DateTimeField(
#         u'绑定时间',
#         blank=True,
#     )
#     device = models.ManyToManyField(
#         'Device',
#     )
#
#     def __unicode__(self):
#         return self.operate_account
#
#     class Meta:
#         verbose_name = u'绑定记录'
#         verbose_name_plural = verbose_name
#
#
# class RemoveBindingRecord(models.Model):
#     """
#     解绑记录
#     """
#     car_identification_num = models.CharField(
#         u'车辆识别码',
#         max_length=30,
#         help_text=u'车辆识别码',
#     )
#     operate_account = models.CharField(
#         u'操作账号',
#         max_length=20,
#     )
#     operation_phone = models.CharField(
#         u'联系电话',
#         max_length=20,
#     )
#     operation_remarks = models.CharField(
#         u'操作备注',
#         default='',
#         max_length=20,
#     )
#
#     device = models.ManyToManyField(
#         'Device',
#     )
#
#     def __unicode__(self):
#         return self.operate_account
#
#     class Meta:
#         verbose_name = u'解绑记录'
#         verbose_name_plural = verbose_name
class Task(models.Model):
    class Meta:
        permissions = (
            ("view_task", "Can see available tasks"),
            ("change_task_status", "Can change the status of tasks"),
            ("close_task", "Can remove a task by setting its status as closed"),
        )








