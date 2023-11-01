from django.contrib import admin
from .models import *


# admin classes
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','dean','hod']


class FacultyAdmin(admin.ModelAdmin):
    list_display = []


# Register your models here.
admin.site.register(Department,admin_class=DepartmentAdmin)
admin.site.register(Faculty)
admin.site.register(Course)

