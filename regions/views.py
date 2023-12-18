from django.shortcuts import render


def view(request):
    return render(
        request,
        'regions.html',
        context={
            'data': [
                ['tt', 'Tashkent', 36, 20],
                ['sd', 'Samarkand', 18, 10],
                ['ny', 'Navoiy', 16, 9],
                ['bo', 'Bukhara', 16, 9],
                ['nn', 'Namangan', 14, 7],
                ['jx', 'Jizzax', 14, 7],
                ['an', 'Andijon', 14, 7],
                ['fa', 'Fergana', 14, 7],
                ['qn', 'Karakalpakstan', 2, 1],
                ['xm', 'Khorazm', 2, 1],
                ['qo', 'Qashqadaryo', 2, 1],
                ['so', 'Surkhandaryo', 1, .5],
                ['sr', 'Sirdarya', 1, .5]
            ],
            'years': [2022, 2023]
        }
    )
