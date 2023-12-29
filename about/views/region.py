from django.shortcuts import render


def region_view(request):
    return render(request, 'about/regions.html')
