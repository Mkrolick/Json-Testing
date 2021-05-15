import json

d = {'q1': 0, 'q2': 0, 'q3': 0, 'q4': 0, 'type_q1': 0}

f = open('1/submissions.json')

jsonResponse = json.load(f)



full_list = []
for sub in jsonResponse["submissions"]:
    list = []
    for i in range(len(d.items())):
        list.append(sub["answers"][i]["answer"])
    full_list.append(list)

sum_list = []
for list in full_list:
    if list == full_list[0]:
        for value in list:
            sum_list.append(value)
    else:
        for i in range(len(list)):
            sum_list[i] = sum_list[i] + list[i]

print(sum_list)
print(full_list)

headers = []
for element in d.keys():
    headers.append(element)

print(headers)


#
#print([x for x in sub["answers"][i][1]])
#list.append([x for x in sub.items()][i][1])
