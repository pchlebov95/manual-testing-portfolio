import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
assert response.status_code == 200

data = response.json()
assert len(data) > 0
assert data[0]['name'] == "Leanne Graham"
assert data[0]['email'] == "Sincere@april.biz"
assert data[0]['address']['city'] == "Gwenborough"
