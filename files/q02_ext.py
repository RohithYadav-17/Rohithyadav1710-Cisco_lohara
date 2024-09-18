import json
patients=[{'id':1,'name':'rohit'},{'id':1,'name':'rahul'}]
with open('q02_patients.json','w') as patients_db:
    json.dump(patients,patients_db)
print('patients entered to json file') 
with open('q02_patients.json','r') as patients_db:
    patients2=json.load(patients_db)
    print(f'reading from json file........\n{patients2}')