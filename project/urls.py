from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('register',views.register,name='register'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('<int:project_id>',views.details,name='details'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), {'template_name': 'registration/Reset_email.html'},
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         {'template_name': 'registration/Reset_Email_Sent.html'}, name='password_reset_done'),
    path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
            auth_views.PasswordResetConfirmView.as_view(), {'template_name': 'registration/Forgot_password.html'},
            name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), {'template_name': 'registration/Signin.html'},
         name='password_reset_complete'),
]
