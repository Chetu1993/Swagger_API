import requests
import random

url = "https://petstore.swagger.io/v2/pet"
headers = {"Content-Type": "application/json"}

# Random ID for testing negative cases
non_existent_id = random.randint(100000, 999999)


response = requests.get(f"{url}/{non_existent_id}", headers=headers)
print("GET non-existent pet status:", response.status_code)  # 404 expected


response = requests.delete(f"{url}/{non_existent_id}", headers=headers)
print("DELETE non-existent pet status:", response.status_code)  # 404 expected


invalid_data = {"id": random.randint(1000, 9999)}
response = requests.post(url, json=invalid_data, headers=headers)
print("POST invalid data status:", response.status_code)
print("POST invalid data body:", response.json())
