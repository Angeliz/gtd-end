# from django.contrib import admin

from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from apiv1.views import UsersViewset


router = DefaultRouter()

# 配置users的url
router.register(r'apiv1', UsersViewset, base_name="users")


apiv1_urlpatterns = [
    re_path('^', include(router.urls)),
]
