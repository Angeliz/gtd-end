# from django.contrib import admin

from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from users.views import UsersViewSet


router = DefaultRouter()

# 配置users的url
router.register(r'users', UsersViewSet, base_name="users")


users_urlpatterns = [
    re_path('^', include(router.urls)),
]
