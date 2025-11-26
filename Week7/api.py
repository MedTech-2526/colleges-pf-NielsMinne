#Get 

import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print(f"Fout bij ophalen: {response.status_code}")

#Post

# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "title": "Nieuwe Post",
#     "body": "Dit is de inhoud van de nieuwe post",
#     "userId": 1
# }

# response = requests.post(url, json=data)

# if response.status_code == 201:
#     print("Post succesvol gecreëerd:", response.json())
# else:
#     print(f"Fout bij aanmaken: {response.status_code}")

#PUT

# url = "https://jsonplaceholder.typicode.com/posts/1"
# data = {
#     "id": 1,
#     "title": "Geüpdatete Post",
#     "body": "Dit is de geüpdatete inhoud van de post",
#     "userId": 1
# }

# response = requests.put(url, json=data)

# if response.status_code == 200:
#     print("Post succesvol bijgewerkt:", response.json())
# else:
#     print(f"Fout bij bijwerken: {response.status_code}")

#PATCH


# url = "https://jsonplaceholder.typicode.com/posts/1"
# data = {
#     "title": "Deel 2 van Geüpdatete Post"
# }

# response = requests.patch(url, json=data)

# if response.status_code == 200:
#     print("Post succesvol gedeeltelijk bijgewerkt:", response.json())
# else:
#     print(f"Fout bij gedeeltelijk bijwerken: {response.status_code}")

#DELETE

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url)

if response.status_code == 200:
    print("Post succesvol verwijderd.")
else:
    print(f"Fout bij verwijderen: {response.status_code}")