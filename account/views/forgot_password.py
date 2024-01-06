from django.shortcuts import render, redirect
from accountsss.models import UserModel
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic import View


class ForgotPasswordView(View):

    @staticmethod
    @login_required('login')
    def get(request):
        return render(request)

    @staticmethod
    @login_required('login')
    def post(request):
        return JsonResponse({'ok': True, 'message': 'success'})
