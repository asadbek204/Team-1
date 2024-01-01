from django.http import JsonResponse
from django.views.generic import View
from competition.models import CompetitionModel
import json


class SearchView(View):

    # @staticmethod
    def get(self, request) -> JsonResponse:
        competitions = CompetitionModel.objects.all()
        competitions = self.serialize(competitions)
        return JsonResponse(
            {
                'competitions': competitions,
                'message': 'success' if competitions else 'No competitions found'
            },
            safe=False
        )

    # @staticmethod
    def post(self, request) -> JsonResponse:
        data = json.loads(request.body)
        competitions = CompetitionModel.objects.filter(**data).order_by('-id')
        competitions = self.serialize(competitions)
        return JsonResponse(
            {
                'competitions': competitions,
                'message': 'success' if competitions else 'No competitions found'
            },
            safe=False
        )

    @staticmethod
    def serialize(competitions: CompetitionModel.objects) -> list:
        return [
            {
                'id': competition.id,
                'title': competition.title,
                'description': competition.description,
                'photo': competition.photo
            } for competition in competitions
        ]
