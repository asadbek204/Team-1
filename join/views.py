from django.shortcuts import render


def joins(request):
    return render(request, template_name='join.html')
