from django.contrib import admin
from django import forms
from .models import Group, Account, UserInfomation

class GroupAdminForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = '__all__'


class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    list_display = ['group_id', 'group_name', 'created', 'last_updated']
    readonly_fields = ['group_id', 'group_name', 'created', 'last_updated']

admin.site.register(Group, GroupAdmin)


class AccountAdminForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = '__all__'


class AccountAdmin(admin.ModelAdmin):
    form = AccountAdminForm
    list_display = ['account_id', 'created', 'last_updated', 'account_password']
    readonly_fields = ['account_id', 'created', 'last_updated', 'account_password']

admin.site.register(Account, AccountAdmin)


class UserInfomationAdminForm(forms.ModelForm):

    class Meta:
        model = UserInfomation
        fields = '__all__'


class UserInfomationAdmin(admin.ModelAdmin):
    form = UserInfomationAdminForm
    list_display = ['name', 'address', 'created', 'last_updated', 'email', 'tel', 'ip_register']
    readonly_fields = ['name', 'address', 'created', 'last_updated', 'email', 'tel', 'ip_register']

admin.site.register(UserInfomation, UserInfomationAdmin)


