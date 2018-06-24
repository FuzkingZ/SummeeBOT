from . import models
from . import serializers
from rest_framework import viewsets, permissions


class GroupViewSet(viewsets.ModelViewSet):
    """ViewSet for the Group class"""

    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class AccountViewSet(viewsets.ModelViewSet):
    """ViewSet for the Account class"""

    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserInfomationViewSet(viewsets.ModelViewSet):
    """ViewSet for the UserInfomation class"""

    queryset = models.UserInfomation.objects.all()
    serializer_class = serializers.UserInfomationSerializer
    permission_classes = [permissions.IsAuthenticated]


