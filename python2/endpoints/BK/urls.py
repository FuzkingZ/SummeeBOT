from django.urls import path, include
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
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Profile
    path('endpoints/profile/', views.ProfileListView.as_view(), name='endpoints_profile_list'),
    path('endpoints/profile/create/', views.ProfileCreateView.as_view(), name='endpoints_profile_create'),
    path('endpoints/profile/detail/<int:pk>/', views.ProfileDetailView.as_view(), name='endpoints_profile_detail'),
    path('endpoints/profile/update/<int:pk>/', views.ProfileUpdateView.as_view(), name='endpoints_profile_update'),
)

urlpatterns += (
    # urls for account
    path('endpoints/account/', views.accountListView.as_view(), name='endpoints_account_list'),
    path('endpoints/account/create/', views.accountCreateView.as_view(), name='endpoints_account_create'),
    path('endpoints/account/detail/<int:pk>/', views.accountDetailView.as_view(), name='endpoints_account_detail'),
    path('endpoints/account/update/<int:pk>/', views.accountUpdateView.as_view(), name='endpoints_account_update'),
)

urlpatterns += (
    # urls for timeline_msg
    path('endpoints/timeline_msg/', views.timeline_msgListView.as_view(), name='endpoints_timeline_msg_list'),
    path('endpoints/timeline_msg/create/', views.timeline_msgCreateView.as_view(), name='endpoints_timeline_msg_create'),
    path('endpoints/timeline_msg/detail/<slug:slug>/', views.timeline_msgDetailView.as_view(), name='endpoints_timeline_msg_detail'),
    path('endpoints/timeline_msg/update/<slug:slug>/', views.timeline_msgUpdateView.as_view(), name='endpoints_timeline_msg_update'),
)

urlpatterns += (
    # urls for message_msg
    path('endpoints/message_msg/', views.message_msgListView.as_view(), name='endpoints_message_msg_list'),
    path('endpoints/message_msg/create/', views.message_msgCreateView.as_view(), name='endpoints_message_msg_create'),
    path('endpoints/message_msg/detail/<int:pk>/', views.message_msgDetailView.as_view(), name='endpoints_message_msg_detail'),
    path('endpoints/message_msg/update/<int:pk>/', views.message_msgUpdateView.as_view(), name='endpoints_message_msg_update'),
)

urlpatterns += (
    # urls for message
    path('endpoints/message/', views.messageListView.as_view(), name='endpoints_message_list'),
    path('endpoints/message/create/', views.messageCreateView.as_view(), name='endpoints_message_create'),
    path('endpoints/message/detail/<int:pk>/', views.messageDetailView.as_view(), name='endpoints_message_detail'),
    path('endpoints/message/update/<int:pk>/', views.messageUpdateView.as_view(), name='endpoints_message_update'),
)

urlpatterns += (
    # urls for timeline
    path('endpoints/timeline/', views.timelineListView.as_view(), name='endpoints_timeline_list'),
    path('endpoints/timeline/create/', views.timelineCreateView.as_view(), name='endpoints_timeline_create'),
    path('endpoints/timeline/detail/<slug:slug>/', views.timelineDetailView.as_view(), name='endpoints_timeline_detail'),
    path('endpoints/timeline/update/<slug:slug>/', views.timelineUpdateView.as_view(), name='endpoints_timeline_update'),
)

