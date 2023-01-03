from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404

def passcard_info_view(request, passcode):
    passcard =  get_object_or_404(Passcard, pk)
    visits =  Visit.objects.filter(passcard__owner_name=passcard)
    for visit in visits:
        this_passcard_visits = [
        {
            'entered_at': visit.entered_at,
            'duration': get_duration(visit),
            'is_strange': is_visit_long(visit, minutes=20)
        }]

        context = {
            'passcard': passcard,
            'this_passcard_visits': this_passcard_visits
        }
        return render(request, 'passcard_info.html', context)



        