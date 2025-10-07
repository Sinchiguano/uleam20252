



# while True:
#     number=int(input('Enter a number, please. \n'))


#     if number % 2==0:
#         print(f'the number {number} entered is even')
#     else:
#         print(f'the number {number} entered is odd')


# userDefault='admin'
# passwordDefault=1234

# user=input('enter the user of the account.\n')
# password=input('enter the password of the account \n')


# if user==userDefault and password==passwordDefault:
#     print('You are allowed to come to the system')
# else:
#     print('you are not user of the system...')


# repository=list()
# ramdonNumber=int(input('Enter a number please\n'))
# sum=0
# for i in range(ramdonNumber):
#     repository.append(i)

# for i in repository:
#     sum=sum+i


# print(f'the total sum is {sum}')

# balance=1000
# choice=input(' 1>deposit\n 2>withdraw \n 3>check balance \n')
# choice=int(choice)
# money=0

# while True:


#     if choice==1:
#         money=int(input('Enter the amount to deposit\n'))
#         balance=balance+money
#         # balance+=money
#     elif choice==2:
#         money=int(input('Enter the amount of money to withdraw.\n'))
#         if balance>money:
#             balance=balance-money
#             print(f'Take your money, please...')
#         else:
#             print('You do not have enough money...')
#     elif choice==3:
#         print(f'The balance is {balance}')
#     else:
#         print('Your choice is not allowed.')
#         # balance-=money

#     choice=input('1>deposit\n 2>withdraw\n 3>check balance\n')
#     choice=int(choice)



# class Students:
#     def __init__(self,name,course='AI'):
#         print('the student has been registered....')
#         self.name=name
#         self.course=course
#     def dataStudent(self):
#         print(f'Name: {self.name} and Course: {self.course}')
#         return


# student1=Students('Cesar')
# student2=Students('Karen', 'Distributed sytems')


# student1.dataStudent()
# student2.dataStudent()


# class Students:
#     def __init__(self,name,course='AI'):
#         print('the student has been registered....')
#         self.name=name
#         self.course=course
#     def dataStudent(self,status='No active'):
#         print(f'Name: {self.name} and Course: {self.course}')
#         return


# student1=Students('Cesar')
# student2=Students('Karen', 'Distributed sytems')


# student1.dataStudent()
# student2.dataStudent()


balance = 1000

while True:
    print("\n=== Banking System ===")
    print("1 > Deposit")
    print("2 > Withdraw")
    print("3 > Check Balance")
    print("4 > Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("⚠️ Invalid input, please enter a number.")
        continue

    if choice == 1:
        money = int(input("Enter the amount to deposit: "))
        balance += money
        print(f"✅ You deposited ${money}. New balance: ${balance}")
    
    elif choice == 2:
        money = int(input("Enter the amount to withdraw: "))
        if money <= balance:
            balance -= money
            print(f"💵 Take your money. Remaining balance: ${balance}")
        else:
            print("❌ Not enough balance.")
    
    elif choice == 3:
        print(f"💰 Your current balance is: ${balance}")
    
    elif choice == 4:
        print("👋 Thank you for using our banking system!")
        break
    
    else:
        print("⚠️ Invalid option, please try again.")
