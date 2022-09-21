from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.shortcuts import redirect
from hashlib import sha256


def login(request):
    return render(request, 'login.html')


def register(request):
    status = request.GET.get('status')
    return render(request, 'register.html', {'status': status})


def validate_registration(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')

    if len(name.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/login/?status=1')

    user = User.objects.filter(email=email)
    if len(user):
        return redirect('/auth/login?status=2')
    try:
        password = sha256(password.encode()).hexdigest()
        user = User(name=name, password=password, email=email)
        user.save()
        return redirect('/auth/login/?status=0')
    except ValueError:
        return redirect('/auth/login/?status=3')
