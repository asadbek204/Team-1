from django.shortcuts import render
from ..models import CounterModel


def results_view(request):
    counter = CounterModel.objects.all()
    return render(request, template_name="about/results.html", context={
        "counter": counter
    })
