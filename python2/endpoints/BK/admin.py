from django.contrib import admin
from django import forms
from .models import Profile, account, timeline_msg, message_msg, message, timeline

class ProfileAdminForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    list_display = ['userid', 'phone', 'email', 'regionCode', 'displayName', 'phoneticName', 'pictureStatus', 'thumbnailUrl', 'statusMessage', 'allowSearchByUserid', 'allowSearchByEmail', 'picturePath', 'musicProfile', 'videoProfile', 'created', 'last_updated']
    readonly_fields = ['userid', 'phone', 'email', 'regionCode', 'displayName', 'phoneticName', 'pictureStatus', 'thumbnailUrl', 'statusMessage', 'allowSearchByUserid', 'allowSearchByEmail', 'picturePath', 'musicProfile', 'videoProfile', 'created', 'last_updated']

admin.site.register(Profile, ProfileAdmin)


class accountAdminForm(forms.ModelForm):

    class Meta:
        model = account
        fields = '__all__'


class accountAdmin(admin.ModelAdmin):
    form = accountAdminForm
    list_display = ['id', 'email', 'created', 'last_updated', 'password', 'auth_token', 'timeline_token', 'qrcodeurl', 'mid', 'Name']
    readonly_fields = ['id', 'email', 'created', 'last_updated', 'password', 'auth_token', 'timeline_token', 'qrcodeurl', 'mid', 'Name']

admin.site.register(account, accountAdmin)


class timeline_msgAdminForm(forms.ModelForm):

    class Meta:
        model = timeline_msg
        fields = '__all__'


class timeline_msgAdmin(admin.ModelAdmin):
    form = timeline_msgAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'code', 'message', 'result', 'writerMid', 'appSn', 'homeId', 'postId', 'status', 'likeCount', 'commentCount', 'postInfo_msg']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'code', 'message', 'result', 'writerMid', 'appSn', 'homeId', 'postId', 'status', 'likeCount', 'commentCount', 'postInfo_msg']

admin.site.register(timeline_msg, timeline_msgAdmin)


class message_msgAdminForm(forms.ModelForm):

    class Meta:
        model = message_msg
        fields = '__all__'


class message_msgAdmin(admin.ModelAdmin):
    form = message_msgAdminForm
    list_display = ['from_mid', 'to_mid', 'createdTime', 'deliveredTime', 'text', 'location', 'hasContent', 'contentType', 'contentPreview', 'contentMetadata', 'sessionId', 'chunks', 'relatedMessageId', 'messageRelationType', 'readCount', 'relatedMessageServiceCode', 'result_code', 'result_msg']
    readonly_fields = ['from_mid', 'to_mid', 'createdTime', 'deliveredTime', 'text', 'location', 'hasContent', 'contentType', 'contentPreview', 'contentMetadata', 'sessionId', 'chunks', 'relatedMessageId', 'messageRelationType', 'readCount', 'relatedMessageServiceCode', 'result_code', 'result_msg']

admin.site.register(message_msg, message_msgAdmin)


class messageAdminForm(forms.ModelForm):

    class Meta:
        model = message
        fields = '__all__'


class messageAdmin(admin.ModelAdmin):
    form = messageAdminForm
    list_display = ['name', 'text', 'created', 'last_updated', 'msgid', 'type', 'packageid', 'stickerid']
    readonly_fields = ['name', 'text', 'created', 'last_updated', 'msgid', 'type', 'packageid', 'stickerid']

admin.site.register(message, messageAdmin)


class timelineAdminForm(forms.ModelForm):

    class Meta:
        model = timeline
        fields = '__all__'


class timelineAdmin(admin.ModelAdmin):
    form = timelineAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'timelineid', 'text', 'picture', 'stickerID', 'packageID']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'timelineid', 'text', 'picture', 'stickerID', 'packageID']

admin.site.register(timeline, timelineAdmin)


