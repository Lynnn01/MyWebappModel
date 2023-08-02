from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hello everyone!")

def about(request):
    return HttpResponse("my name is jetsada Tonsri!")

def contact(request):
    return HttpResponse("this is my contact!")
