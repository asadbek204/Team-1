from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from administration.models import PaymentModel


class PaymentView(CreateView):
    model = PaymentModel
    template_name = 'administration/payment.html'
    fields = ['name', 'phone', 'category', 'card_number', 'summa']
    success_url = '/'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()
        return super().form_valid(form)


class ErrorView(TemplateView):
    template_name = 'administration/error.html'
