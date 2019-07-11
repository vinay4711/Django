from django.shortcuts import render
from . import views
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import request
from django.core.serializers import serialize
import requests
import json
from django.views.generic import View
from .models import Company
# Create your views here.

class CompanySealizedviewlist(View):
    def get(self,request,*args,**kwargs):
        emp=Company.objects.all()
        data=serialize('json',emp)
        #empdata={'eno':emp.eno,'ename':emp.ename,'esal':emp.esal,'eaddr':emp.eaddr}

        #json_data=json.dumps(empdata)
        return HttpResponse(data,content_type='application/json')