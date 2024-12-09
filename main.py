from methods import load_file,save_file

data=load_file("data/user.json")

print(data)

data.append({"name":"TEST"})

save_file("data/user.json",data)




#with open("data/user.json", "r") as file:
#    data = json.load(file)
#    data.append({
 #               "name":"Pero Jonjic",
  #              "age": 56,
 #               "height": 188,
#              "gender": "male"
 #   },)
#print(data)

#with open("data/user.json", "w") as file:
 #   json.dump(data, file, indent=4)