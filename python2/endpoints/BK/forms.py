from django import forms
from .models import Profile, account, timeline_msg, message_msg, message, timeline


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['userid', 'phone', 'email', 'regionCode', 'displayName', 'phoneticName', 'pictureStatus', 'thumbnailUrl', 'statusMessage', 'allowSearchByUserid', 'allowSearchByEmail', 'picturePath', 'musicProfile', 'videoProfile', 'mid']


class accountForm(forms.ModelForm):
    class Meta:
        model = account
        fields = ['id', 'email', 'password', 'auth_token', 'timeline_token', 'qrcodeurl', 'mid', 'Name']


class timeline_msgForm(forms.ModelForm):
    class Meta:
        model = timeline_msg
        fields = ['name', 'code', 'message', 'result', 'writerMid', 'appSn', 'homeId', 'postId', 'status', 'likeCount', 'commentCount', 'postInfo_msg', 'timelineid']


class message_msgForm(forms.ModelForm):
    class Meta:
        model = message_msg
        fields = ['from', 'to', 'deliveredTime', 'text', 'location', 'hasContent', 'contentType', 'contentPreview', 'contentMetadata', 'sessionId', 'chunks', 'relatedMessageId', 'messageRelationType', 'readCount', 'relatedMessageServiceCode', 'result_code', 'result_msg', 'msgid']


class messageForm(forms.ModelForm):
    class Meta:
        model = message
        fields = ['name', 'text', 'msgid', 'type', 'packageid', 'stickerid']


class timelineForm(forms.ModelForm):
    class Meta:
        model = timeline
        fields = ['name', 'timelineid', 'text', 'picture', 'stickerID', 'packageID']


