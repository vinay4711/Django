from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse
from django.http import JsonResponse
import json
import requests
from requests import request
from django.views.generic import View


# Create your views here.

class EmployeeDetailsCBV(View):
    def get(self,request,id,*args,**kwargs):
        emp=Employee.objects.get(id=id)
        empdata={'eno':emp.eno,'ename':emp.ename,'esal':emp.esal,'eaddr':emp.eaddr}
        json_data=json.dumps(empdata)
        return HttpResponse(json_data,content_type='application/json')


