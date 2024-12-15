from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Registration View
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Username already exists'}, status=400)
            else:
                User.objects.create_user(username=username, password=password)
                return redirect('login')
        else:
            return JsonResponse({'error': 'Passwords do not match'}, status=400)
    return render(request, 'accounts/register.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('folder_index')  # Redirect to the main app's homepage
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
    return render(request, 'accounts/login.html')

# Logout View
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
