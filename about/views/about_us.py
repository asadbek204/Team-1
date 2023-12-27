from django.shortcuts import render
from ..models import AdvantagesModel
from account.models import Expert


def about_view(request):
    advantages = AdvantagesModel.objects.all()
    experts = Expert.objects.all()
    return render(request, template_name="about/about-us.html", context={
        "advantages": advantages,
        "experts": experts
    })
