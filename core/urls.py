from core import views
from django.urls import path, include

urlpatterns = [
    path('', views.Home, name='Home'),
    path('login/', views.LogIn, name='LogIn'),
    path('about/', views.About, name='About'),
    path('logout/', views.LogOut, name='LogOut'),
    path('signup/', views.SignUp, name='SignUp'),
    path('contact/', views.Contact, name='Contact'),
    path('change/', views.ChangePassword, name='ChangePassword'),

    path('templates/', include('rtemplates.urls')),

    # Forget Password Missing!
]
