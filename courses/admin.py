from django.contrib import admin

from .models import CourseCategory, CourseDetails


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')


@admin.register(CourseDetails)
class CourseDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category',
        'is_active',
        'course_title',
        'course_image',
        'course_content',
    )
    list_filter = ('category', 'is_active')
    list_editable=('is_active',)