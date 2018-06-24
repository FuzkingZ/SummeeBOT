import unittest
from django.urls import reverse
from django.test import Client
from .models import Profile, account, timeline_msg, message_msg, message, timeline
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_profile(**kwargs):
    defaults = {}
    defaults["userid"] = "userid"
    defaults["phone"] = "phone"
    defaults["email"] = "email"
    defaults["regionCode"] = "regionCode"
    defaults["displayName"] = "displayName"
    defaults["phoneticName"] = "phoneticName"
    defaults["pictureStatus"] = "pictureStatus"
    defaults["thumbnailUrl"] = "thumbnailUrl"
    defaults["statusMessage"] = "statusMessage"
    defaults["allowSearchByUserid"] = "allowSearchByUserid"
    defaults["allowSearchByEmail"] = "allowSearchByEmail"
    defaults["picturePath"] = "picturePath"
    defaults["musicProfile"] = "musicProfile"
    defaults["videoProfile"] = "videoProfile"
    defaults.update(**kwargs)
    if "mid" not in defaults:
        defaults["mid"] = create_account()
    return Profile.objects.create(**defaults)


def create_account(**kwargs):
    defaults = {}
    defaults["id"] = "id"
    defaults["email"] = "email"
    defaults["password"] = "password"
    defaults["auth_token"] = "auth_token"
    defaults["timeline_token"] = "timeline_token"
    defaults["qrcodeurl"] = "qrcodeurl"
    defaults["mid"] = "mid"
    defaults["Name"] = "Name"
    defaults.update(**kwargs)
    return account.objects.create(**defaults)


def create_timeline_msg(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["code"] = "code"
    defaults["message"] = "message"
    defaults["result"] = "result"
    defaults["writerMid"] = "writerMid"
    defaults["appSn"] = "appSn"
    defaults["homeId"] = "homeId"
    defaults["postId"] = "postId"
    defaults["status"] = "status"
    defaults["likeCount"] = "likeCount"
    defaults["commentCount"] = "commentCount"
    defaults["postInfo_msg"] = "postInfo_msg"
    defaults.update(**kwargs)
    if "timelineid" not in defaults:
        defaults["timelineid"] = create_timeline()
    return timeline_msg.objects.create(**defaults)


def create_message_msg(**kwargs):
    defaults = {}
    defaults["from"] = "from"
    defaults["to"] = "to"
    defaults["deliveredTime"] = "deliveredTime"
    defaults["text"] = "text"
    defaults["location"] = "location"
    defaults["hasContent"] = "hasContent"
    defaults["contentType"] = "contentType"
    defaults["contentPreview"] = "contentPreview"
    defaults["contentMetadata"] = "contentMetadata"
    defaults["sessionId"] = "sessionId"
    defaults["chunks"] = "chunks"
    defaults["relatedMessageId"] = "relatedMessageId"
    defaults["messageRelationType"] = "messageRelationType"
    defaults["readCount"] = "readCount"
    defaults["relatedMessageServiceCode"] = "relatedMessageServiceCode"
    defaults["result_code"] = "result_code"
    defaults["result_msg"] = "result_msg"
    defaults.update(**kwargs)
    if "msgid" not in defaults:
        defaults["msgid"] = create_message()
    return message_msg.objects.create(**defaults)


def create_message(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["text"] = "text"
    defaults["msgid"] = "msgid"
    defaults["type"] = "type"
    defaults["packageid"] = "packageid"
    defaults["stickerid"] = "stickerid"
    defaults.update(**kwargs)
    return message.objects.create(**defaults)


def create_timeline(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["timelineid"] = "timelineid"
    defaults["text"] = "text"
    defaults["picture"] = "picture"
    defaults["stickerID"] = "stickerID"
    defaults["packageID"] = "packageID"
    defaults.update(**kwargs)
    return timeline.objects.create(**defaults)


class ProfileViewTest(unittest.TestCase):
    '''
    Tests for Profile
    '''
    def setUp(self):
        self.client = Client()

    def test_list_profile(self):
        url = reverse('endpoints_profile_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_profile(self):
        url = reverse('endpoints_profile_create')
        data = {
            "userid": "userid",
            "phone": "phone",
            "email": "email",
            "regionCode": "regionCode",
            "displayName": "displayName",
            "phoneticName": "phoneticName",
            "pictureStatus": "pictureStatus",
            "thumbnailUrl": "thumbnailUrl",
            "statusMessage": "statusMessage",
            "allowSearchByUserid": "allowSearchByUserid",
            "allowSearchByEmail": "allowSearchByEmail",
            "picturePath": "picturePath",
            "musicProfile": "musicProfile",
            "videoProfile": "videoProfile",
            "mid": create_account().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_profile(self):
        profile = create_profile()
        url = reverse('endpoints_profile_detail', args=[profile.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_profile(self):
        profile = create_profile()
        data = {
            "userid": "userid",
            "phone": "phone",
            "email": "email",
            "regionCode": "regionCode",
            "displayName": "displayName",
            "phoneticName": "phoneticName",
            "pictureStatus": "pictureStatus",
            "thumbnailUrl": "thumbnailUrl",
            "statusMessage": "statusMessage",
            "allowSearchByUserid": "allowSearchByUserid",
            "allowSearchByEmail": "allowSearchByEmail",
            "picturePath": "picturePath",
            "musicProfile": "musicProfile",
            "videoProfile": "videoProfile",
            "mid": create_account().pk,
        }
        url = reverse('endpoints_profile_update', args=[profile.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class accountViewTest(unittest.TestCase):
    '''
    Tests for account
    '''
    def setUp(self):
        self.client = Client()

    def test_list_account(self):
        url = reverse('endpoints_account_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_account(self):
        url = reverse('endpoints_account_create')
        data = {
            "id": "id",
            "email": "email",
            "password": "password",
            "auth_token": "auth_token",
            "timeline_token": "timeline_token",
            "qrcodeurl": "qrcodeurl",
            "mid": "mid",
            "Name": "Name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_account(self):
        account = create_account()
        url = reverse('endpoints_account_detail', args=[account.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_account(self):
        account = create_account()
        data = {
            "id": "id",
            "email": "email",
            "password": "password",
            "auth_token": "auth_token",
            "timeline_token": "timeline_token",
            "qrcodeurl": "qrcodeurl",
            "mid": "mid",
            "Name": "Name",
        }
        url = reverse('endpoints_account_update', args=[account.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class timeline_msgViewTest(unittest.TestCase):
    '''
    Tests for timeline_msg
    '''
    def setUp(self):
        self.client = Client()

    def test_list_timeline_msg(self):
        url = reverse('endpoints_timeline_msg_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_timeline_msg(self):
        url = reverse('endpoints_timeline_msg_create')
        data = {
            "name": "name",
            "code": "code",
            "message": "message",
            "result": "result",
            "writerMid": "writerMid",
            "appSn": "appSn",
            "homeId": "homeId",
            "postId": "postId",
            "status": "status",
            "likeCount": "likeCount",
            "commentCount": "commentCount",
            "postInfo_msg": "postInfo_msg",
            "timelineid": create_timeline().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_timeline_msg(self):
        timeline_msg = create_timeline_msg()
        url = reverse('endpoints_timeline_msg_detail', args=[timeline_msg.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_timeline_msg(self):
        timeline_msg = create_timeline_msg()
        data = {
            "name": "name",
            "code": "code",
            "message": "message",
            "result": "result",
            "writerMid": "writerMid",
            "appSn": "appSn",
            "homeId": "homeId",
            "postId": "postId",
            "status": "status",
            "likeCount": "likeCount",
            "commentCount": "commentCount",
            "postInfo_msg": "postInfo_msg",
            "timelineid": create_timeline().pk,
        }
        url = reverse('endpoints_timeline_msg_update', args=[timeline_msg.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class message_msgViewTest(unittest.TestCase):
    '''
    Tests for message_msg
    '''
    def setUp(self):
        self.client = Client()

    def test_list_message_msg(self):
        url = reverse('endpoints_message_msg_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_message_msg(self):
        url = reverse('endpoints_message_msg_create')
        data = {
            "from": "from",
            "to": "to",
            "deliveredTime": "deliveredTime",
            "text": "text",
            "location": "location",
            "hasContent": "hasContent",
            "contentType": "contentType",
            "contentPreview": "contentPreview",
            "contentMetadata": "contentMetadata",
            "sessionId": "sessionId",
            "chunks": "chunks",
            "relatedMessageId": "relatedMessageId",
            "messageRelationType": "messageRelationType",
            "readCount": "readCount",
            "relatedMessageServiceCode": "relatedMessageServiceCode",
            "result_code": "result_code",
            "result_msg": "result_msg",
            "msgid": create_message().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_message_msg(self):
        message_msg = create_message_msg()
        url = reverse('endpoints_message_msg_detail', args=[message_msg.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_message_msg(self):
        message_msg = create_message_msg()
        data = {
            "from": "from",
            "to": "to",
            "deliveredTime": "deliveredTime",
            "text": "text",
            "location": "location",
            "hasContent": "hasContent",
            "contentType": "contentType",
            "contentPreview": "contentPreview",
            "contentMetadata": "contentMetadata",
            "sessionId": "sessionId",
            "chunks": "chunks",
            "relatedMessageId": "relatedMessageId",
            "messageRelationType": "messageRelationType",
            "readCount": "readCount",
            "relatedMessageServiceCode": "relatedMessageServiceCode",
            "result_code": "result_code",
            "result_msg": "result_msg",
            "msgid": create_message().pk,
        }
        url = reverse('endpoints_message_msg_update', args=[message_msg.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class messageViewTest(unittest.TestCase):
    '''
    Tests for message
    '''
    def setUp(self):
        self.client = Client()

    def test_list_message(self):
        url = reverse('endpoints_message_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_message(self):
        url = reverse('endpoints_message_create')
        data = {
            "name": "name",
            "text": "text",
            "msgid": "msgid",
            "type": "type",
            "packageid": "packageid",
            "stickerid": "stickerid",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_message(self):
        message = create_message()
        url = reverse('endpoints_message_detail', args=[message.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_message(self):
        message = create_message()
        data = {
            "name": "name",
            "text": "text",
            "msgid": "msgid",
            "type": "type",
            "packageid": "packageid",
            "stickerid": "stickerid",
        }
        url = reverse('endpoints_message_update', args=[message.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class timelineViewTest(unittest.TestCase):
    '''
    Tests for timeline
    '''
    def setUp(self):
        self.client = Client()

    def test_list_timeline(self):
        url = reverse('endpoints_timeline_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_timeline(self):
        url = reverse('endpoints_timeline_create')
        data = {
            "name": "name",
            "timelineid": "timelineid",
            "text": "text",
            "picture": "picture",
            "stickerID": "stickerID",
            "packageID": "packageID",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_timeline(self):
        timeline = create_timeline()
        url = reverse('endpoints_timeline_detail', args=[timeline.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_timeline(self):
        timeline = create_timeline()
        data = {
            "name": "name",
            "timelineid": "timelineid",
            "text": "text",
            "picture": "picture",
            "stickerID": "stickerID",
            "packageID": "packageID",
        }
        url = reverse('endpoints_timeline_update', args=[timeline.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


