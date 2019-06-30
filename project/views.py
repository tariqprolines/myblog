from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project,Contact
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    projects=Project.objects.all()[:9]
    return render(request,'project/index.html',{'projects':projects})

def projectlist(request):
    project_list=Project.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(project_list, 9)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    return render(request,'project/projectlist.html',{'projects':projects})

def details(request,project_id):
    project=Project.objects.filter(id=project_id)
    return render(request,'project/details.html',{'project':project[0]})

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
        return redirect('contact')
    else:
        return render(request,'project/contact.html');

@login_required(login_url='/accounts/login/')
def postproject(request):
    if request.method == 'POST':
        project=Project()
        project.title=request.POST.get('title')
        project.description = request.POST.get('description')
        project.image=request.FILES['projectfile']
        project.pub_date=date.today().strftime("%Y-%m-%d");
        project.owner=request.user
        project.save()
        messages.success(request, 'Your Project has been submitted successfully!')
        return redirect('postproject')
    return render(request, 'project/postproject.html')




