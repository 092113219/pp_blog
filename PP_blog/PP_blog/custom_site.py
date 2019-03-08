#!/usr/bin/env python
#! -*- coding:utf-8 -*-
#!@Author: faple
#!@Time: 2019/3/6 10:32

from django.contrib.admin import AdminSite

class CustomSite(AdminSite):
    site_header = 'blog'
    site_title = 'blog管理后台'
    index_title = '首页'

custome_site = CustomSite(name='cus_admin')

