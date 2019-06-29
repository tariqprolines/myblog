from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('<int:project_id>',views.details,name='details'),
    path('projectlist',views.projectlist, name='projectlist'),
    path('postproject',views.postproject,name='postproject'),
]
