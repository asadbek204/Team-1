from django.core.mail import send_mail
from django.shortcuts import render, redirect
from administration.models import ContactModel
from django.conf import settings


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        send_mail(
            name,
            'We will contact soon',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        contacts = ContactModel(name=name, email=email, message=text)
        contacts.save()
    return render(request, 'administration/contact.html')
