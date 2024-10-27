from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class User(AbstractUser):
    pass


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name;


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name;


class BaseModel(models.Model):
    subject = models.CharField(max_length=100, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.subject;

    class Meta:
        abstract = True


class Course(BaseModel):
    description = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="course/%Y/%m")
    category = models.ForeignKey(Category, on_delete=models.PROTECT)


class Lesson(BaseModel):
    content = models.TextField()
    image = models.ImageField(upload_to="lesson/%Y/%m")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Tags = models.ManyToManyField(Tag, related_name='Lesson')
