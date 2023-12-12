from django.shortcuts import render


def view_rules(request):
    return render(request, 'rules.html')
