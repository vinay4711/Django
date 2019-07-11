from django.contrib import admin
from .models import Company
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id','C_Name','C_Class','C_Age','C_Addr']
admin.site.register(Company,CompanyAdmin)
