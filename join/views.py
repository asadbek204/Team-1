from django.shortcuts import render


# Create your views here.
def joins(request):
    return render(request, template_name='join.html')
