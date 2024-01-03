from django.http import JsonResponse
from django.shortcuts import render, redirect
from ..models import UserModel, Participant
from django.views.generic import View
import json


class ProfileView(View):

    @staticmethod
    def get(request):
        # if not request.user.is_authenticated:
        #     return redirect('login')
        # participant = Participant.objects.get(user=request.user)
        return render(request, 'account/profile.html')

    @staticmethod
    def put(request):
        data = json.loads(request.body)
        print(data)
        # UserModel.objects.update(**data)
        return JsonResponse({'ok': True, 'message': 'message successfully printed'})
