from . import models
from . import serializers
from rest_framework import viewsets, permissions , filters
from django_filters.rest_framework import DjangoFilterBackend

class ProfileViewSet(viewsets.ModelViewSet):
    """ViewSet for the Profile class"""

    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class accountViewSet(viewsets.ModelViewSet):
    """ViewSet for the account class"""

    queryset = models.account.objects.all()
    serializer_class = serializers.accountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = models.account.objects.all()
        email = self.request.query_params.get('email', None)
        if email is not None:
            queryset = queryset.filter(email=email)
        return queryset




class timeline_msgViewSet(viewsets.ModelViewSet):
    """ViewSet for the timeline_msg class"""

    queryset = models.timeline_msg.objects.all()
    serializer_class = serializers.timeline_msgSerializer
    permission_classes = [permissions.IsAuthenticated]


class message_msgViewSet(viewsets.ModelViewSet):
    """ViewSet for the message_msg class"""

    queryset = models.message_msg.objects.all()
    serializer_class = serializers.message_msgSerializer
    permission_classes = [permissions.IsAuthenticated]


class messageViewSet(viewsets.ModelViewSet):
    """ViewSet for the message class"""

    queryset = models.message.objects.all()
    serializer_class = serializers.messageSerializer
    permission_classes = [permissions.IsAuthenticated]


class timelineViewSet(viewsets.ModelViewSet):
    """ViewSet for the timeline class"""

    queryset = models.timeline.objects.all()
    serializer_class = serializers.timelineSerializer
    permission_classes = [permissions.IsAuthenticated]


