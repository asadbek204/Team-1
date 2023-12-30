from django.shortcuts import render
from .models import QuestionnaireModel


def competition_view(request):
    return render(request, 'competition/competition.html')


def questionare(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        category = request.POST['category']
        region = request.POST['region']
        phone_number = request.POST['phone_number']
        comment = request.POST['comment']

        join = QuestionnaireModel(first_name=first_name, last_name=last_name, age=age, competition=category,
                                  region=region,
                                  phone_number=phone_number, participant=request.user)
        join.save()
    return render(request, 'competition/join.html')


def detail(request):
    return render(request, 'competition/detail.html')
