#!/usr/bin/env python
#! -*- coding:utf-8 -*-
#!@Author: faple
#!@Time: 2019/3/6 10:50

from django.contrib import admin

class BaseOwnerAdmin(admin.ModelAdmin):
    # 保存数据为当前用户
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)
    # 只显示当前用户的数据
    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)