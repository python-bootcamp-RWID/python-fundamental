users = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 223",
        "city": "Wado",
        "zipcode": "939393-212",
        "geo": {
            "lat": "-38.03023",
            "lng": "82.21212"
        }
    }
}

print(users)
print(users["name"])
print("-" * 50)

for i in users:
    print(f"{i} : {users[i]}")

print(users["address"]["geo"]["lat"])

print("\n---------Konversi Dict to JSON")
# convertion tipe data dict ke json
print(users, type(users))
import json

result = json.dumps(users)
print(result, type(result))

with open('result.json', 'w') as file:
    json.dump(users, file)
