from django.shortcuts import render
from . import models


# Create your views here.
def Home(request):
    context = {}
    students = models.Student.objects.all().order_by("-id")
    context["students"] = students

    return render(request, "index.html", context)


def About(request):
    return render(request, "about.html")


def Contact(request):
    return render(request, "contact.html")


def StudentDetails(request, id):
    context = {}

    student = models.Student.objects.get(id=id)
    context["student"] = student
    return render(request, "details.html", context)
