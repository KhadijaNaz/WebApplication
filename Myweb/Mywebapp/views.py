# Create your views here.
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is Home page.")

def about(request):
    return HttpResponse("This is About page.")    
