from django.urls import path,re_path,include
from . import views
urlpatterns = [
    re_path(r'^register/$',views.register_view,name='register'),
    re_path(r'^login/$',views.login_view,name='login'),
    path(r'^logout/$',views.logout,name='logout'),
    re_path('^', include('django.contrib.auth.urls')),
]
