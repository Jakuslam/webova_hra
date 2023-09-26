import json
 
# Data to be written
f = open("text.txt", "r")
lines = f.readlines()
finalDic = []

for line in lines:
    data = line.split(" ")
    dictionary = {
        "name": data[0],
        "answer one": data[1],
        "answer two": data[2],
        "right Answer": data[3],
    }
    json_object = json.dumps(dictionary, indent=4)
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)


# Serializing json
