import requests
import random
pet_id = random.randint(1000, 9999)
import uuid
pet_id = int(uuid.uuid4().int % 100000)
url = "https://petstore.swagger.io/v2/pet"
headers = {"Content-Type": "application/json"}

# Random ID
pet_id = random.randint(1000, 9999)
data = {"id": pet_id, "name": "pintu", "status": "available"}

def post_request():
    response = requests.post(url=url, json=data, headers=headers)
    print("POST:", response.status_code)
    print(response.json())
    return response.status_code

def get_request():
    response = requests.get(url=f"{url}/{pet_id}", headers=headers)
    print("GET:", response.status_code)
    print(response.json())
    return response.status_code

def put_request():
    update_data = {"id": pet_id, "name": "pintu", "status": "sold"}
    response = requests.put(url=url, json=update_data, headers=headers)
    print("PUT:", response.status_code)
    try:
        print(response.json())
    except ValueError:
        print("No JSON returned")
    return response.status_code

def delete_request():
    response = requests.delete(url=f"{url}/{pet_id}", headers=headers)
    print("DELETE:", response.status_code)
    try:
        print(response.json())
    except ValueError:
        print("No JSON returned")
    return response.status_code


post_request()
get_request()
put_request()
delete_request()
