from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User

# get  --- olmoq
# post --- yubormoq
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            print('ohshadi')
            messages.success(request, 'siz muvafaqiyotli kirdingiz')
            return redirect('/')
        else:
            messages.error(request, 'username yoki password xato')
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        if password != password_confirm:
            messages.error(request, 'Parollar mos emas')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu email allaqachon ro'yxatdan o'tgan!")
            return redirect('register')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        if user is not None:
            auth_login(request, user)
            return redirect('/')

        messages.error(request, "Xatolik yuz berdi")
        return redirect('register')
        
        
    return render(request, 'register.html')


def logout(request):
    auth_logout(request)
    messages.success(request, 'siz muvafaqiyotli chiqdingiz')
    return render(request, 'logout.html')
