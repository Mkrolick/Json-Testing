


full_list = []
submissions = [{"tail" : 2,  "head" : 3 }, {"tail" : 4,  "head" : 5 }]

d = {"tail" : 2,  "head" : 3 }

full_list = []
for sub in submissions:
    list = []
    for i in range(len(sub.items())):
        print([x for x in sub.items()][i][1])
        list.append([x for x in sub.items()][i][1])
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

print([x for x in d.items()])
print(list)
print(full_list)



#
#
#
#for x in range(len(jsonResponse["submissions"])):
#    for i in range(len(d)):
#        key = str([x for x in d.items()][i][0])
#        try:
#            d[key] = d[key] + jsonResponse["submissions"][x]["answers"][i]["answer"]
#            print(d[key])
#        except:
#            pass
#
#
#
#
#
#
#
#
#
#   Archaic Code
#
#    for x in range(len(jsonResponse["submissions"])):
#        for i in range(len(d)):
#            key = str([x for x in d.items()][i][0])
#            try:
#                d[key] = d[key] + jsonResponse["submissions"][x]["answers"][i]["answer"]
#                print(d[key])
#            except:
#                pass


#    # Generates Average list
#    avg = {}
#    for i in range(len(d)):
#        key = str([x for x in d.items()][i][0])
#        avg[key] = d[key]/(len(jsonResponse["submissions"]))
#
#
