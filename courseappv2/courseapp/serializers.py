from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from courseapp.models import Category, Course


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CourseSerializer(ModelSerializer):
    image = serializers.SerializerMethodField(source='image')

    def get_image(self, course):
        if course.image.name.startswith("http"):
            return course.image.name
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri('/static/%s' % course.image.name)

    class Meta:
        model = Course
        fields = '__all__'