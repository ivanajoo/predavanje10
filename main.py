
import json

with open("data.json","r") as file:
    data = json.load(file)
    data.append({
                "name":"Pero Jonjic",
                "age": 56,
                "height": 188,
                "gender": "male"
    },)
print(data)

with open("data.json","w") as file:
    json.dump(data, file, indent=4)