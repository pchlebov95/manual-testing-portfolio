import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
assert response.status_code == 200

data = response.json()
assert len(data) > 0
assert data[0]['name'] == "Leanne Graham"
assert data[0]['email'] == "Sincere@april.biz"
assert data[0]['address']['city'] == "Gwenborough"

request = requests.post(url, json=data[0])
print(request.status_code)

new_user = request.json()
new_id = new_user['id']
print(new_id)

deleted_data =  requests.delete(f"{url}/{new_id}")
print(deleted_data.status_code)
