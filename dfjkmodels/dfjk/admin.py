from django.contrib import admin

# Register your models here.

from dfjk import models
admin.site.register(models.Device)
# admin.site.register(models.BindRecord)
# admin.site.register(models.EnterRecord)
admin.site.register(models.OutRecord)
# admin.site.register(models.RemoveBindingRecord)
