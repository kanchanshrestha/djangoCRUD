from email import message
from urllib import request
from django.shortcuts import redirect, render
from django. http import HttpRequest, HttpResponse,HttpResponseRedirect
from .models import StudentForm
from .forms import StudentF
# Create your views here.

def studentform(request):
    forms=StudentF()
    if request.method=='POST':
        forms=StudentF(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('/studentform/getstudentlist/')
            
        else:
            return HttpResponse("Invalid Form")

    context={
        "forms":forms
    }
  
    return render (request,'studentform/index.html',context)
 
def studentlist(request):
    students=StudentForm.objects.all()
    totalnumber=students.count()
    print("total",totalnumber)
    #FILTERS
    #students=StudentForm.objects.all().order_by('std_id')<<--ASCENDING ORDER
    #students=StudentForm.objects.all().order_by('-std_id')<<--DESCENDING ORDER
    #students=StudentForm.objects.all().exclude(city='pokhara')<<--EXCLUDE
    #students=StudentForm.objects.all().filter(city='pokhara')<<--FILTER
    #students=StudentForm.objects.all()[:3] <<-- LIMIT 3
    #students=StudentForm.objects.all()[7:12] <<-- OFFSER 7 LIMIT 12
    # students=StudentForm.objects.filter(id=2)<<--FILTER
    # a=StudentForm.objects.get(id=2)<<--GET (GET CANNOT RUN IN LOOP WE HAVE TO PRINT IT SEPERATELY)
    studentlist={
        'list':students,
        # 'a':a
        "total":totalnumber
    }
    return render(request,'studentform/student_list.html',studentlist)

def updatestd(request,id):
    student=StudentForm.objects.get(id=id)
    forms=StudentF(instance=student)
    if request.method=='POST':
        forms=StudentF(request.POST,instance=student)
        if forms.is_valid():
            forms.save()
            return redirect ("/studentform/getstudentlist/")
        else:
            return HttpResponse("Invalid Form")
    supdate={
         "forms":forms
    }
    return render(request,'studentform/index.html',supdate)

def deletestd(request,id):
    StudentForm.objects.get(id=id).delete()
    context={
        "message":"deleted"
    }
    return render(request,'studentform/getstudentlist',context)
    return redirect ("/studentform/getstudentlist/")





