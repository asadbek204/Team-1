from django.shortcuts import render, redirect
from account.forms import SignUpForm


def register_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['confirm_password']
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('home')
    return render(request, 'account/register.html', context={
        "form": form
    })
