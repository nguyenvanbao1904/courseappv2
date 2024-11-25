from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from courseapp.models import Category, Course, Lesson, Tag, Comment, User


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

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class LessonSerializer(ModelSerializer):
    Tags = TagSerializer(many=True)
    class Meta:
        model = Lesson
        fields = "__all__"

class LessonDetailSerializer(LessonSerializer):
    class Meta:
        model = LessonSerializer.Meta.model
        fields = '__all__'


class UserSerializer(ModelSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['avatar'] is not None:
            data['avatar'] = instance.avatar.url
        return data

    def create(self, validated_data):
        data = validated_data.copy()
        user = User(**data)
        user.set_password(user.password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'avatar']
        extra_kwargs = {'password': {'write_only': True}}

class CommentSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = '__all__'