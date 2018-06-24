from django.urls import *
from rest_framework import routers
from endpoints import views as lineView
from . import api
from . import views
from material.frontend import urls as frontend_urls
from .views import *
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

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

urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
    path('', views.accountListView.as_view(), name='endpoints_account_list'),
    path('endpoint', views.accountListView.as_view(), name='endpoints_account_list'),
    #path('line/login/',views.loginline_view),
    #re_path(r'^line/login/(?P<acc_id>\d+)$', views.loginline_view, name="loginLineView"),
    path('line/login/<int:id>/', views.loginline_view, name='loginline_view'),
    path('line/logout/<int:id>/', views.logoutline_view, name='logoutline_view'),
    path('line/getpin/<int:id>/', views.getPinByID, name='getPinByID'),
)

urlpatterns += (
    # urls for Profile
    path('profile/', views.ProfileListView.as_view(), name='endpoints_profile_list'),
    path('profile/create/', views.ProfileCreateView.as_view(), name='endpoints_profile_create'),
    path('profile/detail/<int:pk>/', views.ProfileDetailView.as_view(), name='endpoints_profile_detail'),
    path('profile/update/<int:pk>/', views.ProfileUpdateView.as_view(), name='endpoints_profile_update'),
)

urlpatterns += (
    # urls for account
    path('account/', views.accountListView.as_view(), name='endpoints_account_list'),
    path('account/create/', views.accountCreateView.as_view(), name='endpoints_account_create'),
    path('account/detail/<int:pk>/', views.accountDetailView.as_view(), name='endpoints_account_detail'),
    path('account/update/<int:pk>/', views.accountUpdateView.as_view(), name='endpoints_account_update'),
)

urlpatterns += (
    # urls for timeline_msg
    path('timeline_msg/', views.timeline_msgListView.as_view(), name='endpoints_timeline_msg_list'),
    path('timeline_msg/create/', views.timeline_msgCreateView.as_view(), name='endpoints_timeline_msg_create'),
    path('timeline_msg/detail/<slug:slug>/', views.timeline_msgDetailView.as_view(), name='endpoints_timeline_msg_detail'),
    path('timeline_msg/update/<slug:slug>/', views.timeline_msgUpdateView.as_view(), name='endpoints_timeline_msg_update'),
)

urlpatterns += (
    # urls for message_msg
    path('message_msg/', views.message_msgListView.as_view(), name='endpoints_message_msg_list'),
    path('message_msg/create/', views.message_msgCreateView.as_view(), name='endpoints_message_msg_create'),
    path('message_msg/detail/<int:pk>/', views.message_msgDetailView.as_view(), name='endpoints_message_msg_detail'),
    path('message_msg/update/<int:pk>/', views.message_msgUpdateView.as_view(), name='endpoints_message_msg_update'),
)

urlpatterns += (
    # urls for message
    path('message/', views.messageListView.as_view(), name='endpoints_message_list'),
    path('message/create/', views.messageCreateView.as_view(), name='endpoints_message_create'),
    path('message/detail/<int:pk>/', views.messageDetailView.as_view(), name='endpoints_message_detail'),
    path('message/update/<int:pk>/', views.messageUpdateView.as_view(), name='endpoints_message_update'),
)

urlpatterns += (
    # urls for timeline
    path('timeline/', views.timelineListView.as_view(), name='endpoints_timeline_list'),
    path('timeline/create/', views.timelineCreateView.as_view(), name='endpoints_timeline_create'),
    path('timeline/detail/<slug:slug>/', views.timelineDetailView.as_view(), name='endpoints_timeline_detail'),
    path('timeline/update/<slug:slug>/', views.timelineUpdateView.as_view(), name='endpoints_timeline_update'),
)

