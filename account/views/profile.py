from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Participant, UserModel
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
        if password := data.get('password', False):
            if request.user.check_password(password):
                if new_password := data.get('newpassword', False):
                    request.user.set_password(new_password)
                    request.user.save()
                    return JsonResponse({'ok': True, 'message': 'successfully updated'})
                logout(request)
                return JsonResponse({'ok': True, 'message': 'successfully log outed'})
            else:
                return JsonResponse({'ok': False, 'message': 'wrong password'})
        participant_data = {}
        user_data = {}
        for key, value in data.items():
            key = key.split('-')
            if key[0] == 'participant':
                participant_data[key[1]] = value
            else:
                user_data[key[0]] = value
        UserModel.objects.filter(id=request.user.id).update(**user_data)
        Participant.objects.filter(user=request.user).update(**participant_data)
        return JsonResponse({'ok': True, 'message': 'message successfully printed'})
