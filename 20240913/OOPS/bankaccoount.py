class Account:
    def __init__(self,number,name,initial_amount=1000):
        self.__number=number
        self.__name=name
        self.__balance=initial_amount
    def __repr__(self):
        return f'[{self.__name},{self.__number},{self.__balance}]'
    def __str__(self):
        return self.__repr__()
    def deposit(self,amount):
        if amount<0:
            print("enter an positive number")
            return
        self.__balance +=amount
    def withdraw(self,amount):
        if amount>=self.__balance:
            print("no enough balance")
            return
        self.__balance-=amount
rohit_ac = Account(name='Rohit',number='792666411045',initial_amount=3000)
print(rohit_ac)
rohit_ac.deposit(200000)
print(rohit_ac)
rohit_ac.withdraw(50000)
print(rohit_ac)
#print(rohit_ac.__dict__)