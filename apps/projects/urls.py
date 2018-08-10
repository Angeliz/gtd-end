# from django.contrib import admin

from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from projects.views import ProjectsViewSet


router = DefaultRouter()

# 配置users的url
router.register(r'projects', ProjectsViewSet, base_name="projects")


projects_urlpatterns = [
    re_path('^', include(router.urls)),
]