from django.test import TestCase
import requests

#BaseURL='http://127.0.0.1:8000/myapp/'
# Create your tests here.
#Endurl='apijsoncbv'
resp= requests.get('http://127.0.0.1:8000/api/v1/')
data= resp.json()
#print(data)
for d in data:
    idvalue=int(d['id'])
    if idvalue==7:
        print(d['description'])

