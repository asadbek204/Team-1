from django.shortcuts import render


def profile_view(request):
    return render(
        request,
        'profile.html',
        context={
            'competitions': [
                {
                    'img': {'url': 'static/profile/img/competition.png', },
                    'title': 'Испытай себя',
                    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut'
                },
                {
                    'img': {'url': 'static/profile/img/competition.png', },
                    'title': 'Испытай себя',
                    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut'
                },
                {
                    'img': {'url': 'static/profile/img/competition.png', },
                    'title': 'Испытай себя',
                    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut'
                },
                {
                    'img': {'url': 'static/profile/img/competition.png', },
                    'title': 'Испытай себя',
                    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut'
                }
            ]
        }
    )
