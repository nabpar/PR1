from django.contrib import admin
from .models import Student,Teacher
# Register your models here



class StudentAdmin(admin.ModelAdmin):
    list_display=['name','batch']

admin.site.register(Student,StudentAdmin)    

class TeacherAdmin(admin.ModelAdmin):
    list_diasplay=['name','salary','address']

admin.site.register(Teacher,TeacherAdmin)