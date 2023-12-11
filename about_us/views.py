from django.shortcuts import render
from .models import AdvantagesModel, ExpertsModel


def about_view(request):
    advantages = AdvantagesModel.objects.all()
    experts = ExpertsModel.objects.all()
    return render(request, template_name="about-us.html", context={
        "advantages": advantages,
        "experts":experts
    })

