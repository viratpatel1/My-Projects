from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'home.html',{'name':'Hello Virat!'})

def add(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    res = val1 + val2
    
    return render(request,"result.html", {'r':res})