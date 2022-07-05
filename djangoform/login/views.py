from django.shortcuts import redirect, render
from django. http import HttpRequest, HttpResponse,HttpResponseRedirect
from .forms import RegisterF
from .forms import LoginF
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.db import transaction
from login.models import Register
from django.contrib.auth.models import AbstractUser

# Create your views here.
@transaction.atomic
def registerform(request):
    forms=RegisterF()
    if request.method=='POST':
        forms=RegisterF(request.POST)

        if forms.is_valid():
            user=forms.save(commit=False)
            user.set_password(forms.cleaned_data['password'])
            user.is_teacher=1
            user.save()
            # user=Register.objects.create(
            #     username=forms.cleaned_data['username'],
            #     email=forms.cleaned_data['email'],
            #     password=forms.cleaned_data['password'],
            #     passwordconfirmation=forms.cleaned_data['passwordconfirmation']
            # )
            # password=user.set_password(user.password)
            
            # user.save()
            # user.set_password(user.password)
            # password.set_password()
            return redirect('/admin/')
            
        else:
            return HttpResponse(forms.errors)

    context={
        "forms":forms
    }
  
    return render (request,'registration/register.html',context)

def loginform(request):
    forms=LoginF()
    if request.method=='POST':
        forms=LoginF(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            return HttpResponse("user login successfully")
        else:
            return HttpResponse("Invalid Credentials")
            
        # print(forms)

        # if forms.is_valid():

        #     forms.save()
        #     return redirect('/admin/')
            
        # else:
        #     return HttpResponse("Invalid Form")

    context={
        "forms":forms
    }
  
    return render (request,'login/login.html',context)
 