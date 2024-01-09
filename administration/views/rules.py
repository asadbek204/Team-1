from django.shortcuts import render, redirect


def rules(request):
    return render(request, 'administration/pravila.html')
