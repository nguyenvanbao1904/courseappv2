from django.urls import path, include
from rest_framework import routers
from courseapp.views import CategoryViewSet, CourseViewSet, LessonViewSet, UserViewSet

r = routers.DefaultRouter()
r.register('Categories', CategoryViewSet)
r.register('Courses', CourseViewSet)
r.register("Lesson", LessonViewSet)
r.register('User', UserViewSet)


urlpatterns = [
    path('', include(r.urls)),
]
