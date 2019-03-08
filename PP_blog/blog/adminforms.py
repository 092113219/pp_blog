#!/usr/bin/env python
#! -*- coding:utf-8 -*-
#!@Author: faple
#!@Time: 2019/3/6 10:15

from django import forms

class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
