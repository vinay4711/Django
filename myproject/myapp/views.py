from django.http import HttpResponse, request
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def getAge(request):
    return HttpResponse(5)


def LeadName(request):
    return HttpResponse("Amit Joshi")
import json
from django.views.generic import View
#from myproject.myapp import mixings
from . import views,student,durgaview,mixings
#from myproject.myapp.mixings import Httpresponsemixing
class jsonCBV(View,mixings.Httpresponsemixing):
   '''' def get(self, request, *args,**kwargs):
        emp_data = {"name": "vinay", "wife": "sweta", 'mobile': 80877777771}
        # json_data =json.dump(emp_data)
        # resp= 'name {},wife {},mobile {}'.format(emp_data['name'],emp_data['wife'],emp_data['mobile'])
        return JsonResponse(emp_data)'''



   def get(self,request,*args,**kwargs):
       json_data= {'msg':'this is the get method and used '}
       #return render_to_http_response(json_data)
       #return JsonResponse({'msg':'this is the get method and used '})
       return self.render_to_http_response(json_data)
       ##return HttpResponse(json_data,content_type='application/json')
   def post(self,request,*args,**kwargs):
       #json_data= json.dump({'msg':'this is the get method and used '})
       return JsonResponse({'msg':'this is the post method and used '})
       ##return HttpResponse(json_data,content_type='application/json')

