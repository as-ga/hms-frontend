from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
# Create your views here.


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        user_list = User.objects.filter(username=username)
        if not user_list.exists():
            messages.warning(request, 'Account not found ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        if not user:
            messages.warning(request, 'Invalid password ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')


def SignupUser(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('/')
    return render(request, 'accounts/signup.html')


def logoutuser(request):
    logout(request)
    return redirect('/user/login')
