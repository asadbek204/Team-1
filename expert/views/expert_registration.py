from django.shortcuts import render
from django.http import JsonResponse
<<<<<<< HEAD
from account.models import Expert, UserModel
from django.views.generic import View
import json
=======
from account.models import Expert
from django.views.generic import View
>>>>>>> 74ef68f (fixing config:urls.py)


class ExpertRegView(View):

<<<<<<< HEAD
    @staticmethod
    def get(request):
        return render(request, template_name="expert/expert_registration.html")

    @staticmethod
    def post(request):
        data = json.loads(request.body)
        try:
            user = UserModel.objects.get(**data)
        except UserModel.DoesNotExist:
            result = {'ok': False, 'message': 'user does not exist'}
        else:
            try:
                expert = Expert.objects.get(user=user)
            except Expert.DoesNotExist:
                result = {'ok': False, 'message': 'expert does not exist'}
            else:
                result = {'ok': True, 'message': 'success', 'expert': expert}
=======
    def get(self, request):
        return render(request, template_name="expert/expert_registration.html")

    def post(self, request):
        result = {"ok": True}
        print(request.POST)
>>>>>>> 74ef68f (fixing config:urls.py)
        return JsonResponse(result)
