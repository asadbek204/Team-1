from django.shortcuts import render


def certificateview(request):
    return render(request, 'certificate/certificate.html')
