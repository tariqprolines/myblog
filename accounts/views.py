from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect , HttpResponse
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method=='POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        user=authenticate(username = user,password = pwd)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Not Authenticate')
    return render(request,'accounts/login.html')

def logout(request):
    logout(request)
    return redirect('home')

