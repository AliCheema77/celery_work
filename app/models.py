from django.db import models


class ScheduleTime(models.Model):
    ROUTINE_CHOICES = (
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
    )

    email = models.EmailField(max_length=50)
    schedule_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    thrashed = models.CharField(max_length=10, choices=ROUTINE_CHOICES)

    created = models.DateTimeField(auto_now_add=True)
