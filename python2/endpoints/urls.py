from django.conf.urls import url, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'profile', api.ProfileViewSet)
router.register(r'account', api.accountViewSet)
router.register(r'timeline_msg', api.timeline_msgViewSet)
router.register(r'message_msg', api.message_msgViewSet)
router.register(r'message', api.messageViewSet)
router.register(r'timeline', api.timelineViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Profile
    url(r'^endpoints/profile/$', views.ProfileListView.as_view(), name='endpoints_profile_list'),
    url(r'^endpoints/profile/create/$', views.ProfileCreateView.as_view(), name='endpoints_profile_create'),
    url(r'^endpoints/profile/detail/(?P<pk>\S+)/$', views.ProfileDetailView.as_view(), name='endpoints_profile_detail'),
    url(r'^endpoints/profile/update/(?P<pk>\S+)/$', views.ProfileUpdateView.as_view(), name='endpoints_profile_update'),
)

urlpatterns += (
    # urls for account
    url(r'^endpoints/account/$', views.accountListView.as_view(), name='endpoints_account_list'),
    url(r'^endpoints/account/create/$', views.accountCreateView.as_view(), name='endpoints_account_create'),
    url(r'^endpoints/account/detail/(?P<pk>\S+)/$', views.accountDetailView.as_view(), name='endpoints_account_detail'),
    url(r'^endpoints/account/update/(?P<pk>\S+)/$', views.accountUpdateView.as_view(), name='endpoints_account_update'),
)

urlpatterns += (
    # urls for timeline_msg
    url(r'^endpoints/timeline_msg/$', views.timeline_msgListView.as_view(), name='endpoints_timeline_msg_list'),
    url(r'^endpoints/timeline_msg/create/$', views.timeline_msgCreateView.as_view(), name='endpoints_timeline_msg_create'),
    url(r'^endpoints/timeline_msg/detail/(?P<slug>\S+)/$', views.timeline_msgDetailView.as_view(), name='endpoints_timeline_msg_detail'),
    url(r'^endpoints/timeline_msg/update/(?P<slug>\S+)/$', views.timeline_msgUpdateView.as_view(), name='endpoints_timeline_msg_update'),
)

urlpatterns += (
    # urls for message_msg
    url(r'^endpoints/message_msg/$', views.message_msgListView.as_view(), name='endpoints_message_msg_list'),
    url(r'^endpoints/message_msg/create/$', views.message_msgCreateView.as_view(), name='endpoints_message_msg_create'),
    url(r'^endpoints/message_msg/detail/(?P<pk>\S+)/$', views.message_msgDetailView.as_view(), name='endpoints_message_msg_detail'),
    url(r'^endpoints/message_msg/update/(?P<pk>\S+)/$', views.message_msgUpdateView.as_view(), name='endpoints_message_msg_update'),
)

urlpatterns += (
    # urls for message
    url(r'^endpoints/message/$', views.messageListView.as_view(), name='endpoints_message_list'),
    url(r'^endpoints/message/create/$', views.messageCreateView.as_view(), name='endpoints_message_create'),
    url(r'^endpoints/message/detail/(?P<pk>\S+)/$', views.messageDetailView.as_view(), name='endpoints_message_detail'),
    url(r'^endpoints/message/update/(?P<pk>\S+)/$', views.messageUpdateView.as_view(), name='endpoints_message_update'),
)

urlpatterns += (
    # urls for timeline
    url(r'^endpoints/timeline/$', views.timelineListView.as_view(), name='endpoints_timeline_list'),
    url(r'^endpoints/timeline/create/$', views.timelineCreateView.as_view(), name='endpoints_timeline_create'),
    url(r'^endpoints/timeline/detail/(?P<slug>\S+)/$', views.timelineDetailView.as_view(), name='endpoints_timeline_detail'),
    url(r'^endpoints/timeline/update/(?P<slug>\S+)/$', views.timelineUpdateView.as_view(), name='endpoints_timeline_update'),
)

