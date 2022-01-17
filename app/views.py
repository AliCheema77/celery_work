from django.shortcuts import render
from app.forms import ScheduleTimeForm
from django.views import View
from django.contrib import messages


class ScheduleTimeView(View):

    def get(self, request):
        form = ScheduleTimeForm()
        return render(request, 'app/schedule_time.html', {'form': form})

    def post(self, request):
        form = ScheduleTimeForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form data submitted successfully')
            form = ScheduleTimeForm()
            return render(request, 'app/schedule_time.html', {'form': form})
        messages.error(request, "Submitted data is not valid")
        return render(request, 'app/schedule_time.html', {'form': form})
