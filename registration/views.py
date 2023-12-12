from django.shortcuts import render


def view_registration(request):
    return render(request, 'register.html')
