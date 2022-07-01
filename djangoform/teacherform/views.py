from django.shortcuts import redirect, render
from django.http import HttpRequest,HttpResponse
from .models import TeacherForm
from .forms import TeacherF

# Create your views here.

def teacherform(request):
    forms=TeacherF()
    if request.method=='POST':
        forms=TeacherF(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect ("/teacherform/getteacherlist/")
       
        else:
            return HttpResponse("Invalid Form")
    context={
                "forms":forms
            }
    return render(request,'teacherform/index.html',context)

def teacherlist(request):
   teachers=TeacherForm.objects.all()
   totalnumber=teachers.count()
   teacherlist={
        'list':teachers,
        # 'a':a
        "total":totalnumber
    }
   return render(request,'teacherform/teacher_list.html',teacherlist)
   

def updateteach(request,id):
    teacher=TeacherForm.objects.get(id=id)
    forms=TeacherF(instance=teacher)
    if request.method=='POST':
        forms=TeacherF(request.POST,instance=teacher)
        if forms.is_valid():
            forms.save()
            return redirect ("/teacherform/getteacherlist/")
        else:
            return HttpResponse("Invalid Form")
    tupdate={
         "forms":forms
    }

    return render(request,'teacherform/index.html',tupdate)


def deleteteach(request,id):
    TeacherForm.objects.get(id=id).delete()
    return redirect ("/teacherform/getteacherlist/")
   
