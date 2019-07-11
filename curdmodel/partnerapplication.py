import requests
import json
BaseURL="http://127.0.0.1:8000/admin/curdapp/"
ENDURL= 'api'
data_resp=requests.get("http://127.0.0.1:8000/polls/indexapi/")

print(data_resp.text)
print(data_resp.status_code)

