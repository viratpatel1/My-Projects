from django.shortcuts import render
from django.http import HttpResponse
from my_res.models import Contact
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("This is home Page")

def project(request):
    return render(request,"project.html")

def cv(request):
    return render(request,'cv.html')
    
def certificate(request):
    return render(request,"certificate.html")

# def contact(request):
#     models = Contact(request.POST)
#     if models.is_valid():
#         frommail = models.cleaned_data['email']
#         phone = models.cleaned_data['phone']
#         message = models.cleaned_data['message']

#         send_mail(request,subject,message,frommail,['randheer88kumar@gmail.com',frommail])
#     # else:
#     return render(request,"contact.html")








def contact(request):
    if request.method == "POST": 
        name = request.POST['name']
        email = request.POST['email']
        # phone = request.POST['phone']
        message = request.POST['message']



        send_mail(name, message, email,['randheer88kumar@gmail.com',email])

        return render(request,'contact.html' , {'email': email})
    else:
        return render(request,"contact.html")
