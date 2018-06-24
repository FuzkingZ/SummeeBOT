from django.conf.urls import url, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'group', api.GroupViewSet)
router.register(r'account', api.AccountViewSet)
router.register(r'userinfomation', api.UserInfomationViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Group
    url(r'^group/$', views.GroupListView.as_view(), name='Usermanager_group_list'),
    url(r'^group/create/$', views.GroupCreateView.as_view(), name='Usermanager_group_create'),
    url(r'^group/detail/(?P<pk>\S+)/$', views.GroupDetailView.as_view(), name='Usermanager_group_detail'),
    url(r'^group/update/(?P<pk>\S+)/$', views.GroupUpdateView.as_view(), name='Usermanager_group_update'),
)

urlpatterns += (
    # urls for Account
    url(r'^account/$', views.AccountListView.as_view(), name='Usermanager_account_list'),
    url(r'^account/create/$', views.AccountCreateView.as_view(), name='Usermanager_account_create'),
    url(r'^account/detail/(?P<pk>\S+)/$', views.AccountDetailView.as_view(), name='Usermanager_account_detail'),
    url(r'^account/update/(?P<pk>\S+)/$', views.AccountUpdateView.as_view(), name='Usermanager_account_update'),
)

urlpatterns += (
    # urls for UserInfomation
    url(r'^userinfomation/$', views.UserInfomationListView.as_view(), name='Usermanager_userinfomation_list'),
    url(r'^userinfomation/create/$', views.UserInfomationCreateView.as_view(), name='Usermanager_userinfomation_create'),
    url(r'^userinfomation/detail/(?P<pk>\S+)/$', views.UserInfomationDetailView.as_view(), name='Usermanager_userinfomation_detail'),
    url(r'^userinfomation/update/(?P<pk>\S+)/$', views.UserInfomationUpdateView.as_view(), name='Usermanager_userinfomation_update'),
)

