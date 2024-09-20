import json
import requests

class AirplaneApp:
    def __init__(self):
        self.url = 'http://localhost:5000'

    def read_all(self):
        res = requests.get(f'{self.url}/airplanes')
        return res.json()

    def read_by_id(self, id):
        res = requests.get(f'{self.url}/airplanes/{id}')
        return res.json()

    def create(self, airplane_json_str):
        headers = {'Content-type': 'application/json'}
        res = requests.post(f'{self.url}/airplanes', data=airplane_json_str, headers=headers)
        return res.json()

    def update(self, id, airplane_json_str):
        headers = {'Content-type': 'application/json'}
        res = requests.put(f'{self.url}/airplanes/{id}', data=airplane_json_str, headers=headers)
        return res.json()

    def delete(self, id):
        res = requests.delete(f'{self.url}/airplanes/{id}')
        return res.json()

# Main interaction logic
app = AirplaneApp()
choice = int(input('1-all, 2-read_by_id, 3-create, 4-update, 5-delete\nchoice: '))
if choice == 1:
    airplanes = app.read_all()
    print(airplanes)
elif choice == 2:
    id = int(input('id: '))
    airplane = app.read_by_id(id)
    print(airplane)
elif choice == 3:
    model = input('Airplane model: ')
    capacity = int(input('Capacity: '))
    status = input('Status: ')
    airplane_dict = {'model': model, 'capacity': capacity, 'status': status}
    airplane_json_str = json.dumps(airplane_dict)
    airplane = app.create(airplane_json_str)
    print('Airplane created successfully:', airplane)
elif choice == 4:
    id = int(input('id: '))
    old_airplane = app.read_by_id(id)
    if 'message' in old_airplane:
        print(old_airplane['message'])
    else:
        model = input(f'Model ({old_airplane["model"]}): ') or old_airplane["model"]
        capacity = input(f'Capacity ({old_airplane["capacity"]}): ') or old_airplane["capacity"]
        status = input(f'Status ({old_airplane["status"]}): ') or old_airplane["status"]
        airplane_dict = {'model': model, 'capacity': capacity, 'status': status}
        airplane_json_str = json.dumps(airplane_dict)
        airplane = app.update(id, airplane_json_str)
        print('Airplane updated successfully:', airplane)
elif choice == 5:
    id = int(input('id: '))
    old_airplane = app.read_by_id(id)
    print(old_airplane)
    if input('Are you sure to delete? (yes/no) ') == 'yes':
        app.delete(id)
        print('Airplane deleted successfully')
