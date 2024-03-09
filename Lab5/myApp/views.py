from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.urls import reverse

class person:
    
    def __init__(self,userName,passWord):
        self.userName = userName
        self.passWord = passWord
    def __str__(self):
            return self.userName
        

class UserInfoForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password")

# Create your views here.

users = []


# default page 
def index(request):
    return render(request , 'myApp/index.html' , {
        "users":users
    })

def add(request):
            
    if request.method == "POST":
        form = UserInfoForm(request.POST) 

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = person(username,password)

            users.append(user.__str__)

            # sends the user to the defalut page to see what he added 
            return HttpResponseRedirect(reverse("myApp:index"))
    else:
    
        return render(request , 'myApp/addForm.html',{
        "form":UserInfoForm
    })    

