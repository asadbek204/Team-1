from django.shortcuts import render, redirect


def profile(request):
    return render(request, 'account/profile.html')
