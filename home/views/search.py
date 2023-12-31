from django.http import JsonResponse
from django.views.generic import View
from home.models import GalleryModel
import json


class SearchView(View):

    @staticmethod
    def get(request) -> JsonResponse:
        gallery = GalleryModel.objects.all()
        return JsonResponse(gallery, safe=False)

    @staticmethod
    def post(request) -> JsonResponse:
        data = json.loads(request.body)
        gallery = GalleryModel.objects.filter(**data).order_by('-id')
        return JsonResponse(gallery, safe=False)
