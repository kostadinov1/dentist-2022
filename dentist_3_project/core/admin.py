from django.contrib import admin

# Register your models here.
from dentist_3_project.core.models import Appointment, Review


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('venue', 'date', 'time', 'service', 'date_added', 'user')
    list_filter = ('venue', 'date')
    list_per_page = 10


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_added', 'title', 'body')
    list_filter = ('date_added',)
    list_per_page = 10
