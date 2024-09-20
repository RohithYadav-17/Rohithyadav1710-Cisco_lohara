import json
patients=[
    {'id':101,'name':'mahesh'},
    {'id':102,'name':'rohit'},
    {'id':103,'name':'rahul'},
]
patients_str=json.dumps(patients)
print(patients,patients_str)
with open('patients_data.json','w')as patients_db:
    json.dump(patients,patients_db)
patients_list2=json.loads(patients_str)
print(patients_list2,type(patients_list2))
with open('patients_data.json','r')as patients_db:
    patients_list3=json.loads(patients_db)
    print(patients_list3,type(patients_list3))

