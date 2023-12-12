from django.shortcuts import render


def view(request):
    return render(
        request,
        'regions.html',
        context={
            'data': [i for i in range(1, 13)],
            'years': [2022, 2023]
        }
    )
