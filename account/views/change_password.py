from django.shortcuts import render, redirect

def change_password(request):
    return render(request, 'account/change_password.html')