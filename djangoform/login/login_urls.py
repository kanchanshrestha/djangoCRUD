from django.contrib import admin
from django.urls import path
from login import views
urlpatterns = [
    path('login/', views.loginform,name="login"),
   

]