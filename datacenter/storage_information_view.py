from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    in_storage = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    context = {'non_closed_visits': non_closed_visits}
    for visit in in_storage:
        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': visit.format_duration(visit.get_duration())
        })
    return render(request, 'storage_information.html', context)
