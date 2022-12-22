from datacenter.models import *
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    in_storage = Visit.objects.filter(leaved_at__isnull=True)
    for visit in in_storage:
        now_in_storage = visit.passcard.owner_name
        entered_at = visit.entered_at
        duration = localtime()-entered_at    

    non_closed_visits = [
        {
            'who_entered': now_in_storage,
            'entered_at': entered_at,
            'duration': format_duration(duration)
        }
    ]
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
