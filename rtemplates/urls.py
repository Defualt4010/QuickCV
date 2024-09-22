from django.urls import path
from . import views

urlpatterns = [
    path('', views.TempHome, name="TemplatesHome"),
    path('sendMail/', views.SendMail, name="SendMail"),

    path('build/', views.BuildResume, name="Build"),
]
