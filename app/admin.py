from django.contrib import admin
from app.models import ScheduleTime


@admin.register(ScheduleTime)
class ScheduleTimeAdmin(admin.ModelAdmin):
    list_display = ['email', 'schedule_time', 'thrashed', 'created']
