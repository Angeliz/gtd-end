# from django.contrib import admin

from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from todo.views import TodoViewSet


router = DefaultRouter()

# 配置users的url
router.register(r'todo', TodoViewSet, base_name="todo")


todo_urlpatterns = [
    re_path('^', include(router.urls)),
]
