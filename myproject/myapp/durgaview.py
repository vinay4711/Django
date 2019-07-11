from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# dump was using in older version in new version using jsonrespose directly
def empdataview(request):

   emp_data={"name":"vinay","wife":"sweta",'mobile':808771 }
   resp= 'name {},wife {},mobile {}'.format(emp_data['name'],emp_data['wife'],emp_data['mobile'])
   return HttpResponse(resp)
import json
def empdataview_json(request):

   emp_data={"name":"vinay","wife":"sweta",'mobile':80877777771 }
   #json_data =json.dump(emp_data)
   #resp= 'name {},wife {},mobile {}'.format(emp_data['name'],emp_data['wife'],emp_data['mobile'])
   return  JsonResponse(emp_data)
