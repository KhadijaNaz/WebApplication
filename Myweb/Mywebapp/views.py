# Create your views here.
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("This is Home page.")

def about(request):
    return HttpResponse("This is About page.") 

def services(request):
    return HttpResponse("This is services page.")  

def contacts(request):
    return HttpResponse("This is contacts page.")    
