from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, get_user_model

from.forms import LoginForm


def login_view(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form,
    }
    # is_login = None
    if form.is_valid():
        print('hereeee')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            is_login = True
        else:
            is_login = False
        if request.is_ajax():
            print('is ajax')
            data = {
                'isLogin': is_login,
                'loginURL': '/dashboard/'
            }
            return JsonResponse(data)
    return render(request, 'accounts/login_page.html', context)


