
from django.urls import path
from .import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path("first/", views.first , name='first'),
    path("index/", views.index,name="index"),
    path("form_pg/", views.form_pg , name='form_pg'),
    path("signup/",views.signup,name='signup'),
    path("login/",LoginView.as_view(template_name='mapnav/login.html'),name='login'),
    path("logout/",LogoutView.as_view(template_name='mapnav/first.html'),name='logout'),
    path("order/", views.order , name='order'),
    path("activity/", views.activity , name='activity'),
    #path("logout/",auth_views.logout, {next_page : 'mapnav : first'} , name='logout'),
   # path("booking/",views.booking,name='booking'),
    

]