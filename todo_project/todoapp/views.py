from django.shortcuts import render,redirect
from django.views import View
from todoapp.forms import UserRegisterForm,UserLoginForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User  # as form.save doesnot hash password we use user .create method
from django.contrib.auth import authenticate,login,logout

# Create your views here.
class UserRegister(View):
    def get(self,request):
        form=UserRegisterForm()
        return render(request,"register.html",{'form':form})
    def post(self,request):
        form=UserRegisterForm(request.POST)
        if  form.is_valid():# ** from.cleaned_data
            User.objects.create_user(**form.cleaned_data)
            # form.save
            messages.success(request,"Registeration SUccesfull")
            return redirect('u_reg')
            # return redirect("u_login")
            # return HttpResponse("REgistration SUccesfull")
        else:# if another same registeration comes the is valid method fails so 
            return HttpResponse("User with same username  exists")
        
# class UserLoginF
class UserLoginView(View):
    def get(self,request):
        form=UserLoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request):
        username=request.POST.get("username")
        psw=request.POST.get("password")
        res=authenticate(request,username=username,password=psw)
        # authenticate method checks the user table whether the inputtd usename and password are in the table i fthen returns a db object with username as name and if not returns none
        if res:
            return HttpResponse("LoginSUCCESSS")
        else:
            return HttpResponse("Invalid Username")