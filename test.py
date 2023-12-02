import requests
import json

url= "http://127.0.0.1:5000/TESTING"

headers = {
    "ContentType":"application/json"
}
data = {
    "name":"Shanu",
    "age":21
}


response = requests.post(url=url,headers=headers,data=json.dumps(data))
print(response.status_code)
print(response.text)
