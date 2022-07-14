from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, reverse


def home(request):
    return render(request, 'App_auth/home.html')


def login_or_signup(request):
    return render(request, 'App_auth/login_or_signup.html')


def login_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('App_auth:home'))
        elif not User.objects.filter(username=email):
            create_user = User(username=email)
            create_user.set_password(password)
            create_user.save()
            user = authenticate(username=email, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('App_auth:home'))
        else:
            return HttpResponseRedirect(reverse('App_auth:login-or-signup'))

    return HttpResponseRedirect(reverse('App_auth:login-signup'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_auth:home'))
