from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Lesson, Course, Tag


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date', 'category']
    readonly_fields = ['picture']

    def picture(self, course):
        return mark_safe(
            f'<img src = "/static/{course.image.name}" width = "120"/>'
        )


admin.site.register(Category)
admin.site.register(Lesson)
admin.site.register(Course, CourseAdmin)
admin.site.register(Tag)
