
a=10

b=3.5

name="SINCHIGUANO"

is_active=True



print(a,b,name,is_active)


print(type(a))
print(type(name))
print(type(is_active))



device='router'
id=101


print(f'Device: {device} and ID:{id}')


# ARITHMETIC OPERATIONS

numbera=2
numberb=3


# result=numbera+numberb
# print(f"The sum is : {result}")


print("The result of adding two numbers is: ",numbera+numberb)
print("The result of substraction is: ",numbera-numberb)
print("The result is: ",numbera*numberb)
print("The result of power to any number is: ",numbera**numberb)
print("The result is: ",numbera/numberb)
print("The result is: ",numbera//numberb)



#STRINGS
print("#STRINGS")
name="cesar sinchiguano"
print(name.upper())
print(name.capitalize())
name2=name.upper()
print(name2.lower())


language='PYTHON'
print(language[0])
print(language[-1])
print(len(language))


#LIST
print("#LIST")
devices=['router','switch', "cable",45, True, False]
print(len(devices))

print(devices[0])
print(devices[-1])

devices.append('Server')
print(devices)



names=list()
names.append('cesar')
names.append('carlos')
names.append('julio')
names.append('pedro')
print(names)
names[1]='sebastian'
print(names)
print(names.pop())
print(names)


numbers=list(range(10))
print(numbers)
selectednumbers=numbers[2:4]
print(selectednumbers)

print(numbers[:-1])
print(numbers[:3])

numbers[2:3]=[100,100]
print(numbers)

#TUPLES
print('#TUPLES')


containertuple=(10,20)



print(containertuple[0])
containerlist=list(containertuple)
print(type(containerlist))


#DICTIONARY
print('#TUPLES')

animals={'dog':'nice','cat':'pretty','monkey':'black'}

print(animals['cat'])


animals['cat']='ugly'
print(animals)

print('turtle' in animals)



del animals['monkey']
print(animals)

animals['monkey']='ugly'
animals['mouse']='tiny'
animals['donkey']='big'



# for item in animals:
#     feature=animals[item]
#     print("%s is %s" % (item,feature))


myDictionary={'person':2,'cat':4, 'spider':8}


for key in myDictionary:
    numbersOfLegs=myDictionary[key]
    print("The %s has %d"%(key, numbersOfLegs))


# CONDITIONALS

print('# CONDITIONALS')


latency=80
if latency<50:
    print('LOW LATENCY')
elif latency==0:
    print('MEDIUM LATENCY ')
else:
    print('HIGH LATENCY')




#LOOPS

for i in range(10):
    print(i)


counter=0
while counter<10:
    print('I am counting from 0 to 210', f'Actual number {counter}')
    # counter=counter+1
    counter+=1




#INPUT
# print('# INPUTS')
# name=input('Enter your name, please \n')
# print(f'Hello my worthy: {name}')




squareNumbers=list()
for i in range(10):
    squareNumbers.append(i*i)
print(squareNumbers)



squareNumbersV2=[i*i for i in range(10)]
print(squareNumbersV2)


name='Cesar Augusto Sinchiguano Chiriboga'
letterInDictionary={}
for letter in name:
    letterInDictionary[letter]=letterInDictionary.get(letter, 0)+1
print(letterInDictionary)




lista=[1,2,3]
listb=[11,22,33]
newList=[lista,listb]
print(newList)
print(newList[1][2])




# MULTIPLE CONDITIONS

age=20
student=True
if age < 18 and student:
    print('ADULT STUDENT')


# BREAK AND CONTINUE

for i in range(10):
    print(f'The current number is {i}')
    if i == 5:
        break



for i in range(5):
    if i==3:
        continue
    print(f'The current number is {i}')




# FUNCTIONS

def greetings(name):
    return f"Hello {name}"


tmpName=greetings('santiago')
print(tmpName)




#FUNCTIONS WITH DEFAULT VARIABLES
def connect(device="Router"):
    print(f'connecting to {device}...')

connect()

connect('switch')


# LOOP WITH DICTIONARY

device={'router':'active','switch':'inactive','server':'active'}


for name, status in device.items():
    print(f'{name}:{status}')


# REVERSE STRING
text="python"
rev=""

for char in text:
    rev=char+rev

print(rev)

print('ok!!!')