from django.contrib.auth import login, authenticate,logout as auth_logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from .forms import RegisterForm
from project.models import Project
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
            return redirect('dashboard')
        else:
            messages.success(request, 'Username or Password is not correct!')
    return render(request,'accounts/login.html')

@login_required(login_url='/accounts/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })

def logout(request):
    auth_logout(request)
    return render(request, 'accounts/logout.html')

@login_required(login_url='/accounts/login/')
def dashboard(request):
    project_list=Project.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(project_list, 9)
    try:
        projectall = paginator.page(page)
    except PageNotAnInteger:
        projectall = paginator.page(1)
    except EmptyPage:
        projectall = paginator.page(paginator.num_pages)

    projects=Project.objects.filter(owner_id=request.user.id)
    user=get_object_or_404(User,pk=request.user.id)

    return render(request,'accounts/dashboard.html',{'projectall':projectall,'projects':projects,'user':user})

@login_required(login_url='/accounts/login/')
def editproject(request,p_id):
    project=get_object_or_404(Project,pk=p_id)
    if request.method=='POST':
        proj=Project()
        proj.title=request.POST.get('title')
        proj.description = request.POST.get('description')
        update = Project.objects.filter(id=p_id).update(title=proj.title,description=proj.description)
        print(update)
        if update:
            messages.success(request, 'Your project has been updated successfully!')
            return redirect('dashboard')
        else:
            messages.success(request, 'Something Wrong!')
    return render(request, 'accounts/editproject.html',{'project':project})

@login_required(login_url='/accounts/login/')
def deleteproject(request,p_id):
    delproject=Project.objects.filter(id=p_id).delete()
    if delproject:
        messages.success(request, 'Your project has been deleted successfully!')
        return redirect('dashboard')

def editprofile(request):
    return HttpResponse("Profile Edit Page")