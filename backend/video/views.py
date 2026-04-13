from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.

from .utils import create_unique_uuid

@login_required
def new_meet_view(request):
    room_id = create_unique_uuid()
    redirect_url = f'/{room_id}'
    return redirect(redirect_url)

@login_required
def meet_view(request, room_id=None):
    context = {
        'room_id': room_id
    }
    return render(request, 'video/index.html', context=context)