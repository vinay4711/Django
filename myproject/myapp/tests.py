from django.test import TestCase
import requests

BaseURL='http://127.0.0.1:8000/myapp/'
# Create your tests here.
Endurl='apijsoncbv'
resp= requests.get('http://127.0.0.1:8000/myapp/apijsoncbv')
data= resp.json()
#print(data)
print(resp.text)