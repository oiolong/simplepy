import json


txt = './CPlayerlist.txt'
txts_file = open(txt,'r')
#txts = txts_file.read()
lines = txts_file.readlines()
arr = []

for line in lines:
    line_arr = line.split(',')
    arr.append(line_arr)
   
with open('CPlayerlist.json','w') as CPlayerlist_dumped :
    json.dump(arr,CPlayerlist_dumped)

txts_file.close()
