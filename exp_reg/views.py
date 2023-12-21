from django.shortcuts import render


def exp_reg_view(request):
    return render(request, template_name="exp_reg.html")

