from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homeview(request,*args,**kwargs):
   # return HttpResponse("<h2>Welcome to the store</h3>")
   return render(request,'home.html',{})

def aboutview(request,*args,**kwargs):
    #return HttpResponse("<h2>About us</h3>")
    return render(request,'aboutus.html',{})



def contactview(request,*args,**kwargs):
    #return HttpResponse("<h2>Contact us</h3>")
    return render(request,'contactus.html',{})


def serviceview(request,*args,**kwargs):
    #return HttpResponse("<h1> socialpages</h3>")
    return render(request,'services.html',{})

