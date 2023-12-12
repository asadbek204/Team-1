from django.shortcuts import render
from django.views.generic import ListView
from .models import GalleryModel



# Create your views here.
<<<<<<< HEAD
class GalleryListView(ListView):
    model = GalleryModel
    template_name = 'gallery.html'
    context_object_name = 'obj'
    paginate_by = 9

    def get_queryset(self):
        return GalleryModel.objects.all()
=======
def gallery(request):
    return render(request, 'gallery.html')
>>>>>>> c9565aa (gallery almost done media left)
