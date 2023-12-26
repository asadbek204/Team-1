from django.shortcuts import render
from .models import GalleryModel

# Create your views here.
def home(request):
    return render(request, 'home/main_page.html')


def gallery(request):
    return render(request, 'home/gallery.html')
