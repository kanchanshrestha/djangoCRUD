from django.contrib import admin
from django.urls import path
from studentform import views
urlpatterns = [
    path('', views.studentform,name="add_student"),
    path('getstudentlist/',views.studentlist,name="getstudentlist"),
    path('updatestudent/<int:id>',views.updatestd,name="updates"),
    path('deletestudent/<int:id>',views.deletestd,name="deletes")
]
