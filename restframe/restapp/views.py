from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import request
from django.core.serializers import serialize
import requests
import json
from django.views.generic import View
from .mixings import JsonResponseMixin
from .models import Employee,update
# Create your views here.
def update_model_detailsview(request):
    data={
        'count':100,
        'content':"where are going to meet someone with HTPP response"
    }
    #return JsonResponse(data)
    json_data=json.dumps(data)
    return HttpResponse(json_data,content_type='application/json')


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content json view 1"
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
     def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content json view 2"
        }
        return self.render_to_json_response(data)



class EmployeeDetailsCBV(View):
    def get(self,request,*args,**kwargs):
        emp=Employee.objects.get(id=2)
        empdata={'eno':emp.eno,'ename':emp.ename,'esal':emp.esal,'eaddr':emp.eaddr}
        json_data=json.dumps(empdata)
        return HttpResponse(json_data,content_type='application/json')

class EmployeeSealizedviewlist(View):
    def get(self,request,*args,**kwargs):
        emp=Employee.objects.all()
        data=serialize('json',emp)
        #empdata={'eno':emp.eno,'ename':emp.ename,'esal':emp.esal,'eaddr':emp.eaddr}

        #json_data=json.dumps(empdata)
        return HttpResponse(data,content_type='application/json')

class UpdateSealizedviewlist(View):
    def get(self,request,*args,**kwargs):
        upd=update.objects.all()
        data=serialize('json',upd,fields={'user','content','timestamp'})
        #empdata={'eno':emp.eno,'ename':emp.ename,'esal':emp.esal,'eaddr':emp.eaddr}

        #json_data=json.dumps(empdata)
        return HttpResponse(data,content_type='application/json')