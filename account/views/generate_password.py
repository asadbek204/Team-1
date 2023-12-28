from django.shortcuts import render, redirect

def generate_password(request):
    return render(request , template_name='account/generator password.html')