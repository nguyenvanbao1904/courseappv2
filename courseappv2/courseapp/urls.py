from django.urls import path, include
from courseapp.admin import admin_site
from rest_framework import routers
from courseapp.views import CategoryViewSet, CourseViewSet

r = routers.DefaultRouter()
r.register('Categories', CategoryViewSet)
r.register('Courses', CourseViewSet)


urlpatterns = [
    path('', include(r.urls)),
]
