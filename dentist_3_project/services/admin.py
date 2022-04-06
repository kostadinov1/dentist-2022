from django.contrib import admin

# Register your models here.
from dentist_3_project.services.models import Service, BlogPost


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('treatment', 'category', 'duration', 'price')
    list_filter = ('category',)
    list_per_page = 10


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('date_added', 'title', 'body')
