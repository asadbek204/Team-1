from django.contrib import admin
from .models import PaymentModel

@admin.register(PaymentModel)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_display_links = ['name', 'created_at']

