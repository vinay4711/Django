from django.contrib import admin
from .models import update ,Employee
from .models_Student import Studnet

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','eno','ename','esal','eaddr']
admin.site.register(Employee,EmployeeAdmin)


class UpdatesAdmin(admin.ModelAdmin):
    list_display = ['id','user','content','updated','timestamp']
admin.site.register(update,UpdatesAdmin)

class StudnetAdmin(admin.ModelAdmin):
    list_display = ['id','S_Name','S_Class','s_Age','s_mobile']
admin.site.register(Studnet,StudnetAdmin)