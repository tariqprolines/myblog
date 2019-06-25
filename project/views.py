from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Project,Contact
def home(request):
    projects=Project.objects.all()
    return render(request,'project/index.html',{'projects':projects})
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
        return redirect('/contact')
    else:
        return render(request,'project/contact.html');
def register(request):
    return render(request,'project/register.html')
def login(request):
    return HttpResponse('Login')