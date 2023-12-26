from django.shortcuts import render
from django.views.generic import ListView

from .models import GalleryModel


# Create your views here.
def home(request):
    return render(request, 'home/main_page.html')


class GalleryListView(ListView):
    model = GalleryModel
    template_name = 'home/gallery.html'
    context_object_name = 'obj'
    paginate_by = 9

    def get_queryset(self):
        return GalleryModel.objects.all()
