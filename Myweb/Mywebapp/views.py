# Create your views here.
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context={
        "variable":"spime",
        "variable1":"password manager"
    }

    return render(request, 'index.html',context)
    #return HttpResponse("This is Home page.")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is About page.") 

def services(request):
    return render(request, 'service.html')
    #return HttpResponse("This is services page.")  

def contacts(request):
    return render(request, 'contact.html')
    #return HttpResponse("This is contacts page.")    

