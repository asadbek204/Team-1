from django.shortcuts import render
from ..models import UserModel


def profile(request):
    return render(request, 'account/profile.html')
