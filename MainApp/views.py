from django.shortcuts import render
from . import models


# Create your views here.
def Home(request):
    context = {}
    students = models.Student.objects.all().order_by("-id")

    for student in students:
        student.prefix_str = getModelChoice(student.prefix, models.prefix_choices)

    context["students"] = students

    return render(request, "index.html", context)


def About(request):
    return render(request, "about.html")


def Contact(request):
    return render(request, "contact.html")


def StudentDetails(request, id):
    context = {}
    students = models.Student.objects.filter(id=id)
    for student in students:
        student.prefix_str = getModelChoice(student.prefix, models.prefix_choices)
        context["student"] = student
    return render(request, "details.html", context)


def getModelChoice(num, choices):
    for choice in choices:
        if choice[0] == num:
            return choice[1]
