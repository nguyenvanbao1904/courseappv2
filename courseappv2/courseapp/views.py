from rest_framework import viewsets, generics, request, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from courseapp.models import Category, Course, Lesson, User
from courseapp.paginators import ItemPaginator
from courseapp.serializers import CategorySerializer, CourseSerializer, LessonSerializer, CommentSerializer, \
    UserSerializer


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = ItemPaginator

    def get_queryset(self):
        query = self.queryset
        cate_id = self.request.query_params.get("category")
        if cate_id:
            query = query.filter(category_id=cate_id).all()

        kw = self.request.query_params.get("kw")
        if kw:
            query = query.filter(subject__icontains=kw)
        return query

    @action(detail=True, methods=["get"], url_path="lessons")
    def get_lessons(self, request, pk=None):
        course = self.get_object()
        serialize = LessonSerializer(course.lesson_set.prefetch_related("Tags"), many=True)
        return Response(serialize.data)

class LessonViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Lesson.objects.prefetch_related("Tags").filter(active=True).all()
    serializer_class = LessonSerializer
    pagination_class = ItemPaginator

    @action(methods=["get"], detail=True, url_path="comments")
    def get_comments(self, request, pk=None):
        ls = self.get_object()
        serializer = CommentSerializer(ls.comment_set.select_related('user').all(), many=True)
        return Response(serializer.data)

class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=["get"], detail=False, url_path="current-user", permission_classes=[permissions.IsAuthenticated])
    def get_current_user(self, request):
        user = request.user
        return Response(UserSerializer(user).data)


