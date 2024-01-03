from django.contrib.auth import login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from account.models import UserModel
import json


class LoginView(View):

    @staticmethod
    def get(request):
        if not request.user.is_authenticated:
            return render(request, 'account/login.html')
        return redirect('profile')

    @staticmethod
    def post(request):
        try:
            username, password = json.loads(request.body).items()
            try:
                user = UserModel.objects.get(username=username, password=password)
            except UserModel.DoesNotExist:
                return JsonResponse({'ok': False, 'message': 'user not found'})
            else:
                login(request, user)
                return JsonResponse({'ok': True, 'message': 'successfully logged in'})
        except ValueError:
            return JsonResponse({'ok': False, 'message': 'wrong parameters'}, status=404)
