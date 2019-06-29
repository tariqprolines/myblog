from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Project(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=RichTextField(blank=True, null=True)
    image=models.ImageField(upload_to='project/images',default='')
    pub_date=models.DateField()
    owner= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Contact(models.Model):
    contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, default='')
    email=models.EmailField()
    phone=models.CharField(max_length=30,default='')
    message=models.TextField(default='')
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name




