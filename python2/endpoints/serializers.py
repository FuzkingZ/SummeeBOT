from . import models

from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Profile
        fields = (
            'pk', 
            'userid', 
            'phone', 
            'email', 
            'regionCode', 
            'displayName', 
            'phoneticName', 
            'pictureStatus', 
            'thumbnailUrl', 
            'statusMessage', 
            'allowSearchByUserid', 
            'allowSearchByEmail', 
            'picturePath', 
            'musicProfile', 
            'videoProfile', 
            'created', 
            'last_updated', 
        )


class accountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.account
        fields = (
            'pk', 
            'id', 
            'email', 
            'created', 
            'last_updated', 
            'password', 
            'auth_token', 
            'timeline_token', 
            'qrcodeurl', 
            'mid', 
            'Name', 
        )


class timeline_msgSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.timeline_msg
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'code', 
            'message', 
            'result', 
            'writerMid', 
            'appSn', 
            'homeId', 
            'postId', 
            'status', 
            'likeCount', 
            'commentCount', 
            'postInfo_msg', 
        )


class message_msgSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.message_msg
        fields = (
            'pk', 
            'from_mid', 
            'to_mid', 
            'createdTime', 
            'deliveredTime', 
            'text', 
            'location', 
            'hasContent', 
            'contentType', 
            'contentPreview', 
            'contentMetadata', 
            'sessionId', 
            'chunks', 
            'relatedMessageId', 
            'messageRelationType', 
            'readCount', 
            'relatedMessageServiceCode', 
            'result_code', 
            'result_msg', 
        )


class messageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.message
        fields = (
            'pk', 
            'name', 
            'text', 
            'created', 
            'last_updated', 
            'msgid', 
            'type', 
            'packageid', 
            'stickerid', 
        )


class timelineSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.timeline
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'timelineid', 
            'text', 
            'picture', 
            'stickerID', 
            'packageID', 
        )


