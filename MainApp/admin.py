from django.contrib import admin

# Register your models here.
from .models import Student, Major


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("std_id", "prefix", "name", "lastname", "phone", "major")
    search_fields = list_display


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = list_display
