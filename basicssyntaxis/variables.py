
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

for item in animals:
    feature=animals[item]
    print("%item has %feature" % (item,feature))
print('ok!!!')