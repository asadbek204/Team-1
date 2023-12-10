from django.contrib import admin
from .models import GalleryModel


# Register your models here.
@admin.register(GalleryModel)
class GalleryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['title']