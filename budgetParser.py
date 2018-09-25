import sys
import re
import json

with open(sys.argv[1]) as f:
    jsonData = json.load(f)

labels={}
for i in jsonData["Map"]:  
    jsonlabel = i["label"] 
    jsonIndexdata = i["keywords"]
    
    labels[jsonlabel] = jsonIndexdata

with open(sys.argv[2], 'r') as transFile:
    data=transFile.read()
    data=re.sub('  +', '###', data)

transactions = {}

for line in data.splitlines():
    if line[0]=="0" or line[0]=="1":
        line = line[13:]
        endOfDisc = line.find("###")
        description = line[:endOfDisc]
        value = line[endOfDisc+3:]
        endOfValue = value.find("###")
        value = value[:endOfValue].replace(",","")
        value = float(value)

        if description in transactions:
            transactions[description] += value
        else:
            transactions[description] = value
               
final = {}

noMatch = []

for key, value in transactions.items():
    tagFound=False
    for catag, tags, in labels.items():
        for label in tags:
            if label in key and tagFound==False:
                if catag in final:
                    final[catag] +=value
                else:
                    final[catag] = value
                tagFound=True
    if tagFound == False:
        noMatch.append(key)

for finalKey, finalVal in final.items():
    print(finalKey + " = " + str(finalVal))

print("---------There were " +str(len(noMatch)) + " transactions not matched")
for descr in noMatch:
    print(descr)
