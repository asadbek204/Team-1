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
            user = UserModel.objects.get(username=data['username'], password=data['password'])
        except UserModel.DoesNotExist:
            result = {'ok': False, 'message': 'user does not exist'}
        else:
            try:
                expert = Expert.objects.get(user=user)
            except Expert.DoesNotExist:
                result = {'ok': False, 'message': 'expert does not exist'}
            else:
                result = {'ok': True, 'message': 'success'}
        return JsonResponse(result)

    def put(self, request):
        data = json.loads(request.body)
        user = UserModel.objects.filter(username=data.get('username')).first()
        data = self.post()
        expert = Expert.objects.get(user=request.user)
        if data.get('newusername', False) and data.get('newpassword', False):
            expert.user.username = data['newusername']
            expert.user.set_password(data['newpassword'])
            expert.user.save()
            login(request, expert.user)
        return JsonResponse({'ok': True, 'message': 'success'})
