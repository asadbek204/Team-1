from django.shortcuts import render


def competition_view(request):
    return render(request, 'competition/competition.html')
