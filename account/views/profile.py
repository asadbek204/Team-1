from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Participant
from django.views.generic import View
import json


class ProfileView(View):

    @staticmethod
    @login_required(login_url='login')
    def get(request):
        participant = Participant.objects.get(user=request.user)
        return render(request, 'account/profile.html', context={'participant': participant})

    @staticmethod
    @login_required(login_url='login')
    def put(request):
        data = json.loads(request.body)
        request.user.update(**data)
        return JsonResponse({'ok': True, 'message': 'message successfully printed'})
