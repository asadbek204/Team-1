from django.shortcuts import render


def view(request):
    return render(request, 'payment.html')