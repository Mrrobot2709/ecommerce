from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context = {
        "title": "Hello"
    }
    return render(request,"home_page.html",context)

def about_page(request):
    return render(request,"home_page.html",{})

def contact_page(request):
    context = {
        "title": "Hello",
        "content":"Welcome to login page"
    }
    return render(request,"contact/view.html",context)