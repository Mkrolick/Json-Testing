import  json


f = open('json.json',)

# returns JSON object as
# a dictionary
jsonResponse = json.load(f)

# Iterating through the json
# list
#for key in data:
#    print(key)

# 5 answers    d = {"type_q3" : 0, "type_q2": 0}
list = [11, 12]
d = {"type_q3" : 0, "type_q2": 0}



for x in range(len(jsonResponse["submissions"])):
    for i in range(len(d)):
        key = str([x for x in d.items()][i][0])
        try:
            d[key] = d[key] + jsonResponse["submissions"][x]["answers"][i]["answer"]
            print(d[key])
        except:
            pass



print(d)



jsonResponse["submissions"][0]["answers"]










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
