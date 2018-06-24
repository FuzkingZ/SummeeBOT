#from django.core.urlresolvers import reverse
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Group(models.Model):

    # Fields
    group_id = models.AutoField(primary_key=True)#extension_fields.AutoSlugField(populate_from='AccountForm')
    group_name = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('Usermanager_group_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('Usermanager_group_update', args=(self.pk,))


class Account(models.Model):

    # Fields
    account_id = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    account_password = models.CharField(max_length=30)

    # Relationship Fields
    acc_grp_id = models.ForeignKey(Group,on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('Usermanager_account_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('Usermanager_account_update', args=(self.pk,))


class UserInfomation(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    address = models.TextField( blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    email = models.EmailField(max_length=200)
    tel = models.CharField(max_length=10)
    ip_register = models.GenericIPAddressField()
  #  special_list = models.IntegerField()
    # Relationship Fields
    uid = models.ForeignKey(
        Account, on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('Usermanager_userinfomation_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('Usermanager_userinfomation_update', args=(self.pk,))


