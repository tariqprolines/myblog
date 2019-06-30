from django.urls import path,re_path,include
from . import views
urlpatterns = [
    re_path(r'^register/$',views.register_view,name='register'),
    re_path(r'^login/$',views.login_view,name='login'),
    re_path(r'^logout/$',views.logout,name='logout_account'),
    re_path('^', include('django.contrib.auth.urls')),

    # Dashboard

    re_path(r'^dashboard/$',views.dashboard, name='dashboard'),
    path('dashboard/<int:p_id>',views.editproject, name='editproject'),
]
