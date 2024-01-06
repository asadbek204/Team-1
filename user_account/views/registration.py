from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from user_account.forms import SignUpForm
from user_account.models import Participant, School
from about.models import Region


def register_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['confirm_password']
            country, city = form.cleaned_data['region'].split()
            region = Region.objects.get(name=city, country=country)
            school_name, number = form.cleaned_data['school'].split(':')
            school = School.objects.get(school_name=school_name, number=number)
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            participant = Participant.objects.create(user=user, region=region,
                                                     school=school)
            participant.save()
            authenticate(request, username=user.username, password=form.cleaned_data['password'])
            return redirect('login')
    regions = Region.objects.all()
    return render(request, 'account/signup.html', context={
        "form": form,
        'regions': regions
    })
