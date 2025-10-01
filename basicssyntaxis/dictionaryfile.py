

mydictionary=dict()
mydictionary['humans']=2
mydictionary['mouse']=4
mydictionary['spider']=8

for animal in mydictionary:
    data=mydictionary[animal]
    print('the %s has %d'%(animal,data))

# LOOPS

counter=0
while counter<10:
    print(counter)
    # counter=counter+1
    counter+=1

# name=input('Enter your name: \n')
# print(f'Hello, {name}')



myList=list()
for i in range(10):
    if i%2==0:
        myList.append(i)

print(myList)

print('*******')
myList=[ i for i in range(10) if i%2==0]
print(myList)
print('ok....')

print('*******')
myList=[ i*i for i in range(100)]
print(myList)
print('ok....')


def greetings():
    return f'Hello my friend...'



tmp=greetings()
print(tmp)

def greetings2(name='friend'):
    print(f'Hello, {name}')
    return 


# greetings2('Cesar')
greetings2()

while True:
    numbera=int(input('Enter the first number\n'))
    numberb=input('Enter the second number \n')
    numberb=int(numberb)


    operationType=input('Enter numbers from 1 to 4. \n 1 adding \n 2 substract \n 3 multiply \n 4 division')
    if int(operationType)==1:
        result=numbera+numberb