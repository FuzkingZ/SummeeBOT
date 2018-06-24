import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Group, Account, UserInfomation
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


def create_group(**kwargs):
    defaults = {}
    defaults["group_id"] = "group_id"
    defaults["group_name"] = "group_name"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_account(**kwargs):
    defaults = {}
    defaults["account_password"] = "account_password"
    defaults.update(**kwargs)
    if "acc_grp_id" not in defaults:
        defaults["acc_grp_id"] = create_group()
    return Account.objects.create(**defaults)


def create_userinfomation(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["address"] = "address"
    defaults["email"] = "email"
    defaults["tel"] = "tel"
    defaults["ip_register"] = "ip_register"
    defaults.update(**kwargs)
    if "uid" not in defaults:
        defaults["uid"] = create_account()
    return UserInfomation.objects.create(**defaults)


class GroupViewTest(unittest.TestCase):
    '''
    Tests for Group
    '''
    def setUp(self):
        self.client = Client()

    def test_list_group(self):
        url = reverse('Usermanager_group_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_group(self):
        url = reverse('Usermanager_group_create')
        data = {
            "group_id": "group_id",
            "group_name": "group_name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_group(self):
        group = create_group()
        url = reverse('Usermanager_group_detail', args=[group.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_group(self):
        group = create_group()
        data = {
            "group_id": "group_id",
            "group_name": "group_name",
        }
        url = reverse('Usermanager_group_update', args=[group.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AccountViewTest(unittest.TestCase):
    '''
    Tests for Account
    '''
    def setUp(self):
        self.client = Client()

    def test_list_account(self):
        url = reverse('Usermanager_account_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_account(self):
        url = reverse('Usermanager_account_create')
        data = {
            "account_password": "account_password",
            "acc_grp_id": create_group().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_account(self):
        account = create_account()
        url = reverse('Usermanager_account_detail', args=[account.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_account(self):
        account = create_account()
        data = {
            "account_password": "account_password",
            "acc_grp_id": create_group().pk,
        }
        url = reverse('Usermanager_account_update', args=[account.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class UserInfomationViewTest(unittest.TestCase):
    '''
    Tests for UserInfomation
    '''
    def setUp(self):
        self.client = Client()

    def test_list_userinfomation(self):
        url = reverse('Usermanager_userinfomation_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_userinfomation(self):
        url = reverse('Usermanager_userinfomation_create')
        data = {
            "name": "name",
            "address": "address",
            "email": "email",
            "tel": "tel",
            "ip_register": "ip_register",
            "uid": create_account().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_userinfomation(self):
        userinfomation = create_userinfomation()
        url = reverse('Usermanager_userinfomation_detail', args=[userinfomation.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_userinfomation(self):
        userinfomation = create_userinfomation()
        data = {
            "name": "name",
            "address": "address",
            "email": "email",
            "tel": "tel",
            "ip_register": "ip_register",
            "uid": create_account().pk,
        }
        url = reverse('Usermanager_userinfomation_update', args=[userinfomation.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


