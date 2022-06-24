from django.contrib import admin
from django.urls import path
from teacherform import views
urlpatterns = [
    path('',views.teacherform,name="add_teacher"),
    path('getteacherlist/',views.teacherlist,name="getteacherlist"),
    path('updateteacher/<int:id>',views.updateteach,name="updatet"),
    path('deleteteacher/<int:id>',views.deleteteach,name="deletet")

]
