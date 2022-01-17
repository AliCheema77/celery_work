from django import forms
from app.models import ScheduleTime
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class ScheduleTimeForm(forms.ModelForm):

    class Meta:
        model = ScheduleTime
        fields = ('email', 'schedule_time', 'thrashed')
        widgets = {
            'schedule_time': DateTimePickerInput()
        }
