from pprint import pprint

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login
from account.models import Expert, UserModel
import json
from django.views.generic import View


class ExpertRegView(View):

    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            return redirect('matching')
        return render(request, template_name="expert/expert_registration.html")

    @staticmethod
    def post(request):
        data = json.loads(request.body)
        try:
            user = UserModel.objects.get(username=data['username'])
        except UserModel.DoesNotExist:
            result = {'ok': False, 'message': 'user does not exist'}
        else:
            if user.check_password(data['password']):
                try:
                    expert = Expert.objects.get(user=user)
                except Expert.DoesNotExist:
                    result = {'ok': False, 'message': 'expert does not exist'}
                else:
                    result = {'ok': True, 'message': 'success'}
            else:
                result = {'ok': False, 'message': 'wrong password'}
        return JsonResponse(result)

    def put(self, request):
        response = self.post(request)
        data = json.loads(response.__dict__['_container'][0])
        if not data.get('ok'):
            return response
        data = json.loads(request.body)
        (_, username), (_, password), (_, newusername), (_, newpassword) = data.items()
        print(username, password, newusername, newpassword)
        user = UserModel.objects.get(username=data['username'])
        if data.get('newusername', False) and data.get('newpassword', False):
            user.username = newusername
            user.set_password(newpassword)
            user.save()
            login(request, user)
            return JsonResponse({'ok': True, 'message': 'success'})
        return JsonResponse({'ok': False, 'message': 'change your information'})