from django.contrib.auth import authenticate
from django.shortcuts import render
from user_account.models import Expert, UserModel


def create_expert(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = UserModel.objects.create(username=username)
        user.set_password(password)
        user.save()
        expert = Expert(user=user)
        expert.save()
        authenticate(request, username=username, password=password)
    return render(request, template_name='administration/create_expert.html')
