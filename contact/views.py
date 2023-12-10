from django.shortcuts import render


def contact_view(request):
    return render(request, 'contact.html')


def profile_view(request):
    return render(request, 'profile.html')


def password_reset_view(request):
    return render(request, template_name='forgot password.html')