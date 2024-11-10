from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.safestring import mark_safe

from .models import Category, Lesson, Course, Tag


class CourseAdminSite(admin.AdminSite):
    def get_urls(self):
        return [path("courses-stats/", self.stats)] + super().get_urls()

    def stats(self, request):
        stats = Category.objects.annotate(count=Count('course__id')).values('id', 'name', 'count')
        return TemplateResponse(request, "./admin/stats.html", {
            "stats" : stats
        })


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date', 'category']
    readonly_fields = ['picture']

    def picture(self, course):
        return mark_safe(
            f'<img src = "/static/{course.image.name}" width = "120"/>'
        )


admin_site = CourseAdminSite()

admin_site.register(Category)
admin_site.register(Lesson)
admin_site.register(Course, CourseAdmin)
admin_site.register(Tag)
