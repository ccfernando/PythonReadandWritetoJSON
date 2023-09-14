import json
# JavaScript Object Notation (JSON)
# JSON is a lightweight data-interchange format ·
# is a plain text written in JavaScript object notation {"key":value, "anotherKey":"anothervalue"}

# creating a python dictionary
characterDetail={}
# Dictionaries are used to store data values in key:value pairs.
# e.g. thisdict = {"Name": "Chimken", "Ability": "Egg laying", "Age": 64}

# Adding key-value pairs in characterDetail dictionary
characterDetail["name"] = input("Please Enter Name: ")
characterDetail["ability"] = input("Please Enter Ability: ")
characterDetail["personality"] = input("Please Enter Personality: ")

# printing a dictionary
print(characterDetail)

# getting the 'values' from a dictionary using their 'keys' using .get()
# and saving it to a variable
name = characterDetail.get("name")
ability = characterDetail.get("ability")
personality = characterDetail.get("personality")

# Printing the name variable
print("Hello ", name)

# saving to a json file

# opening  the json file connection with write mode
outfile = open("./resource/CharInfo.json","w")

# dumping the contents of the  charDetail dict to the json file
json.dump(characterDetail, outfile)

# closing the json file connection
outfile.close()


# opening  the json file connection with read mode
file = open("./resource/CharInfo.json", "r")

# creating a python dict that will store the contents
# of the json file
aDict = json.loads(file.read())

# printing the newly created dict from the json file
print(aDict)

# closing the json file connection
file.close()

name2 = aDict.get("name")
print("Hello ", name2)
