import json

#load and loads
#dump and dumps

with open(r'sample.json','r') as jf:
    data=json.load(jf)
for x in data['people'][0].keys():
    print(x + " ===> "+ str(data['people'][0][x] ))

info={
    'Name':'Navnath Satre',
    'City':'Pune',
    'Tech':['Python','AIML','AWS'],
    'Manager': False,
    'Salary':None
}
#
# with open('trainer_info.json','w') as wjf:
#     json.dump(info,wjf)