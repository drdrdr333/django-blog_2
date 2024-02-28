from django.shortcuts import render
from django.http import Http404
from polling.models import Poll

# Create your views here.
def list_view(request):
    context = {'polls': Poll.objects.all()}
    return render(request, 'polling/list.html', context)

def detail_view(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':
        if request.POST.get('vote') == 'Yes':
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()
    context = {'poll': poll}
    return render(request, 'polling/detail.html', context)