from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    # return HttpResponse("this is my view")
    contax = {
        "variable" : "this is my web site"
    }
    # messages.success(request,"this is the test message")
    return render(request,"index.html",contax)

def about(request):
    # return HttpResponse("this is my about")
    return render(request, "about.html")

def services(request):
    # return HttpResponse("this is my services")
    return render(request, "services.html")

def contact(request):
    # return HttpResponse("this is my request")
    #adding data into database
    if request.method == "POST":
        username = request.POST.get('username')
        username1 = request.POST.get('username1')
        recipt = request.POST.get('recipt')
        urlname = request.POST.get('urlname')
        textarea = request.POST.get('textarea')
        cost = request.POST.get('cost')
        contact = Contact(username = username,username1 = username1,recipt = recipt,urlname = urlname,textarea = textarea,cost = cost)
        contact.save()
        messages.success(request, 'our message is sent....')
    return render(request, "contact.html")