from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Group, Account, UserInfomation
from .forms import GroupForm, AccountForm, UserInfomationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator





@method_decorator(login_required, name='dispatch')
class GroupListView(ListView):
    model = Group

@method_decorator(login_required, name='dispatch')
class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm

@method_decorator(login_required, name='dispatch')
class GroupDetailView(DetailView):
    model = Group

@method_decorator(login_required, name='dispatch')
class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm

@method_decorator(login_required, name='dispatch')
class AccountListView(ListView):
    model = Account

@method_decorator(login_required, name='dispatch')
class AccountCreateView(CreateView):
    model = Account
    form_class = AccountForm

@method_decorator(login_required, name='dispatch')
class AccountDetailView(DetailView):
    model = Account

@method_decorator(login_required, name='dispatch')
class AccountUpdateView(UpdateView):
    model = Account
    form_class = AccountForm

@method_decorator(login_required, name='dispatch')
class UserInfomationListView(ListView):
    model = UserInfomation

@method_decorator(login_required, name='dispatch')
class UserInfomationCreateView(CreateView):
    model = UserInfomation
    form_class = UserInfomationForm

@method_decorator(login_required, name='dispatch')
class UserInfomationDetailView(DetailView):
    model = UserInfomation

@method_decorator(login_required, name='dispatch')
class UserInfomationUpdateView(UpdateView):
    model = UserInfomation
    form_class = UserInfomationForm

