import requests
import json

url= "https://servertest2-kw7i.onrender.com/TESTING"

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
