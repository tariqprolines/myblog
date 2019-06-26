from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate,logout
from django.shortcuts import render, redirect , HttpResponse
from django.contrib import messages
from .models import Project,Contact
from .forms import RegisterForm

def home(request):
    projects=Project.objects.all()
    return render(request,'project/index.html',{'projects':projects})
def details(request,project_id):
    project=Project.objects.filter(id=project_id)
    return render(request,'project/details.html',{'project':project[0]})

@login_required
def about(request):
    return render(request,'project/about.html')

def contact(request):
    if request.method=='POST':
        contact=Contact()
        contact.name=request.POST.get('name','')
        contact.email=request.POST.get('email','')
        contact.phone=request.POST.get('phone','')
        contact.message=request.POST.get('message','')
        contact.save()
        messages.success(request,'Your query has been submitted successfully, We will contact you shortly!')
        return redirect('/contact')
    else:
        return render(request,'project/contact.html');

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'project/register.html', {'form': form})

def login(request):
    if request.method=='POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        user=authenticate(username = user,password = pwd)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Not Authenticate')
    return render(request,'project/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')