from django import forms
from .models import Group, Account, UserInfomation
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit , Row
from crispy_forms.helper import FormHelper

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_id', 'group_name']


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_id','account_password', 'acc_grp_id']


class UserInfomationForm(forms.ModelForm):
    class Meta:
        model = UserInfomation
        fields = ['name', 'address', 'email', 'tel', 'ip_register', 'uid']

class RegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(label="Email Address")
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm password")
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    gender = forms.ChoiceField(choices=((None, ''), ('F', 'Female'), ('M', 'Male'), ('O', 'Other')))
    receive_news = forms.BooleanField(required=False, label='I want to receive news and special offers')
    agree_toc = forms.BooleanField(required=True, label='I agree with the Terms and Conditions')

    layout = Layout('username', 'email',
                    Row('password', 'password_confirm'),
                    Fieldset('Pesonal details',
                             Row('first_name', 'last_name'),
                             'gender', 'receive_news', 'agree_toc'))
