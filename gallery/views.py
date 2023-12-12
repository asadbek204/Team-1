from django.shortcuts import render
from django.views.generic import ListView
from .models import GalleryModel
from django import template

tem = template.Library()


# Create your views here.

class GalleryListView(ListView):
    model = GalleryModel
    template_name = 'gallery.html'
    context_object_name = 'obj'
    paginate_by = 9

    def get_queryset(self):
        return GalleryModel.objects.all()
