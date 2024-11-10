from rest_framework import viewsets, generics

from courseapp.models import Category, Course
from courseapp.paginators import ItemPaginator
from courseapp.serializers import CategorySerializer, CourseSerializer


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


