class Dog:
    def __init__(self, name):
        self.name=name 

    def feature(self):
        return f'The dog name is {self.name}'
    


dog1=Dog('chester')


print(dog1.feature())


class Car:
    def __init__(self, brand, year):
        self.brand=brand
        self.year=year

    def informationCar(self):
        return f' {self.brand}, {self.year}'




car1=Car('Toyota', 2020)
car2=Car('Tesla',2023)


print(car1.informationCar())
print(car2.informationCar())

        



class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount
        return f'Deposited {amount}, new balance={self.balance}'
    
    def withdraw(self, amount):
        if amount>self.balance:
            return 'Insufficient funds'
        self.balance-=amount
        return f'withdraw {amount}, new balance={self.balance}'


client1=BankAccount('Cesar', 100)

print(client1.deposit(650))
print(client1.withdraw(100))
print(client1.withdraw(20))
