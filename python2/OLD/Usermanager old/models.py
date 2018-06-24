# -*- coding: utf-8 -*-
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from django.db import models

# Create your models here.

class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=200)
   # group_type = models.IntegerField(default=1)
    def __str__(self):
        return self.group_name

class Account(models.Model):
    account_group = models.ForeignKey(Group, on_delete=models.CASCADE)
    account_id = models.CharField(max_length=200)
    account_password = models.CharField(max_length=200)
    last_join = models.CharField(max_length=200)
    def __str__(self):
        return self.account_id

class UserInfomation(models.Model):
    uid = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    ip_register = models.CharField(max_length=200)
    def __str__(self):
        return self.name