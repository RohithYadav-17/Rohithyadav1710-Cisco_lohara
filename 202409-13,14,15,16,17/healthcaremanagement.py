patients=[]
def patient_add(patient):
    global patients
    patients.append(patient)
def patient_delete(patient):
    global patients
    try:
        patients.remove(patient)
    except ValueError as err:
        print("No data regarding that patient id")
    
def display_patients():
    
    if patients:
        print("current patients")
        for patient in patients:
            print(f"{patients}")
        else:
            print("no patients in list")
        
def menu():
    choice=int(input('''1.add
2.delete
3.display patients
4.exit
your choice....'''))
    if choice == 1:
        patient= (input('enter the patient name:'))
        patient_add(patient)
    elif choice ==2:
        patient=(input('enter the patient name:'))
        patient_delete(patient)
    elif choice == 3:
        display_patients()
def menus():
    choice=menu()
    while choice !=4:
        choice=menu()
    print('app ended')

menus()