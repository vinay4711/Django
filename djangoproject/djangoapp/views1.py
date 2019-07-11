from django.http import HttpResponse
from django.template import response
from django.shortcuts import render
from django.template import loader
import request
import request

def index(request):
    #template=loader.get_template('index1.html')
    template = loader.get_template('index1.html')  # getting our template
    name = {
        'student': 'rahul',
        'Age':89.,
        'salary':9000
    }
    return HttpResponse(template.render(name))  # rendering the template in HttpResponse