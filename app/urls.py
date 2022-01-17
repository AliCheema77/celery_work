from django.urls import path
from app.views import ScheduleTimeView

urlpatterns = [
    path("schedule/", ScheduleTimeView.as_view(), name="schedule"),
]
