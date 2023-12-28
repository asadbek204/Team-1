from django.shortcuts import render, redirect

def email(request):
    return render(request, template_name='account/email.html')