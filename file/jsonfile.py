# # write dictionary data to Json file
# import  json
# batchinfo = {
#     "Trainers = Santhosh"
#     "Batch = Morning"
#     "Time = 8am to 9am"
#     "No of students = 20"
# }
#
# Students = {
#     "Boys": [
#         {"name": "venkatesh", "age": 25, "place": "chennai"},
#         {"name": "Makarand", "age": 24, "place": "Mumbai"},
#         {"name": "Sreenivas", "age": 26, "place": "Bangalore"},
#         {"name": "Jayaram", "age": 22, "place": "Hyderabad"},
#         {"name": "Santhosh", "age": 28, "place": "Kochi"}
#     ],
#
#     "Girls": [
#         {"name": "Navya", "age": 23, "place": "USA"}
#     ]
# }
#
# fvar = open(r'python batch.jason.','w')
# json.dump(Students,fvar)
# fvar.close()
# print("filecreated")

# Reading Data from Json file
# import json
# fjson = open(r'cred.json', 'r')
# data = json.load(fjson)
# fjson.close()
#
# print(data)

### another exmple using personalinfo.json
import json
fvar = open(r'personalinfo.json','r')
alldata = json.load(fvar)
fvar.close()
# print(alldata)
# girlsdata = alldata['Girls']
# for x in girlsdata:
#     if (x['place'] == "Banglore"):
#         print(x['name'])

girlsdata = alldata['Girls']
for x in girlsdata:
    if (x['place'] == "Bangalore"):
        print(x['name'])