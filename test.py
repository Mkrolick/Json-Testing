import  json


f = open('json.json',)

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
#for key in data:
#    print(key)

# 5 answers
for i in range(len(data["submissions"])):
    for dict in data["submissions"][i]["answers"]:
        print(dict)
    for dict in data["submissions"][i]["answers"]:
        try:
            print(dict["answer"])
        except:
            pass

# Closing file
f.close()

#
#
#[0]["id"]
#
#
#
#
#
#
#
