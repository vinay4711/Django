from django.http import  HttpResponse
from django.http import JsonResponse
class Httpresponsemixing():
    def render_to_http_response(self,json_data):
        return JsonResponse(json_data,content_type='application/json')