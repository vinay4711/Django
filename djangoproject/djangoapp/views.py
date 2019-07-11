from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hello(request):
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")

from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
@require_http_methods(["GET"])
def show(request):
    return HttpResponse('<h1>This is Http GET request.</h1>')

#@require_http_methods(["POST"])
#def show(request):
   #return HttpResponse('<h1>This is Http Post request.</h1>')


from django.shortcuts import render
# importing loading from django template
from django.template import loader
# Create your views here.
from django.http import HttpResponse

def index(request):
    template = loader.get_template('javascript.html')  # getting our template
    return HttpResponse(template.render())  # rendering the template in HttpResponse
