from django.urls import path
from MainApp.views import *
urlpatterns = [
    path("", home),
    path("about", about),
    path("contact", contact),
]