from . import models

from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Group
        fields = (
            'pk', 
            'group_id', 
            'group_name', 
            'created', 
            'last_updated', 
        )


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Account
        fields = (
            'pk', 
            'account_id', 
            'created', 
            'last_updated', 
            'account_password', 
        )


class UserInfomationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserInfomation
        fields = (
            'pk', 
            'name', 
            'address', 
            'created', 
            'last_updated', 
            'email', 
            'tel', 
            'ip_register', 
        )


