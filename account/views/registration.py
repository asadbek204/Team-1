from django.shortcuts import render, redirect


def register_view(request):
    return render(request, 'account/register.html')
