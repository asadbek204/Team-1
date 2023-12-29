from django.shortcuts import render
from django.http import JsonResponse
from account.models import Expert
from django.views.generic import View


class ExpertRegView(View):

    def get(self, request):
        return render(request, template_name="expert/expert_registration.html")

    def post(self, request):
        result = {"ok": True}
        print(request.POST)
        return JsonResponse(result)
