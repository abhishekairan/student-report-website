from django.contrib import admin
from .models import * 

admin.site.site_header  = "Admin"


# models admin classes
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','course','email']

class MarksAdmin(admin.ModelAdmin):
    list_display = ['student_name','subject_name','mark','totalMarks']



# Register your models here.

admin.site.register(Student,StudentAdmin)
admin.site.register(Marks,MarksAdmin)