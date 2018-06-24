# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Group,Account,UserInfomation

admin.site.register(Group)
admin.site.register(Account)
admin.site.register(UserInfomation)