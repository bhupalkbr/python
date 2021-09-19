#Functions
#syntax - def functionName(parameters):
#				statements
from functools import reduce

def evenOrOdd(number):
    "this function is used to check whether the given number is even or odd"
    if(number%2==0):
        print('{} is even'.format(number))
    else:
        print('{} is odd'.format(number))
        
evenOrOdd(19)
evenOrOdd(18)
evenOrOdd(22)
print(evenOrOdd.__doc__)
print(print.__doc__)

# function to return values

def cubeOfNumber(number):
    cube = number*number*number
    return cube
    
result = cubeOfNumber(10)
print(result)

#callculate marks

def calculate(myMarks):
    myMarks[2] = 70
    
marks = [80,98,32,78,89]
calculate(marks)
print(marks)

# Default arguments

def defaultArg(x=10):
    print(x)
    
defaultArg(60)
defaultArg()

# keyword arguments

def bioData(name,gender,location,phonenum):
    print('name: {} gender: {} location: {} phonenum: {}'.format(name,gender,location,phonenum))
    
bioData('Bhupal','M','Manikonda',8939)
bioData(location='Manikonda',gender='M',phonenum=8939,name='Bhupal')

#variable number of arguments

# *args(normal arguments/ non keyword arguments
# **kwargs(keyword arguments)

def printAll(*args):
    for arg in args:
        print(arg)
    
printAll(1,10,20,80,90,100,101,102)

def multiply(start,*args):
    mult=start
    for num in args:
        mult = mult*num
    return mult
        
result = multiply(10,1,2,3,4)
print(result)

#kwargs
def bioData(**kwargs):
    for key,value in kwargs.items():
        print('{}:{}'.format(key,value))
        
bioData(name='Bhupal',gender='M',phonenum=8939,loc='Manikonda',pin='123')

def eatMe(apple,banana,grapes):
    print(apple,banana,grapes)
    
fruits = (10,5,21)
eatMe(*fruits)

# Generator Function & Generator objects

def coconutCapacity(num):
    calories = num * 9
    yield calories
    print('Super')
    
calories = coconutCapacity(2)
for i in calories:
    print(i)
    
    
# Ananymous function - lambda
# lambda arguments:expression
# Function can have any number of arguments but only one expression

cube = (lambda num:num*num*num)(3)
print(cube)

cube = lambda num:num*num*num
print(cube(3))

# Filter
# filter(function,iterable)

def isEven(num):
    return num%2==0
    
numbers = [10,11,23,22,80,87]
result = filter(isEven,numbers)
print(list(result))

numbers = [10,11,23,22,80,87]
result = filter(lambda num:num%2==0,numbers)
print(list(result))

# map(function,iterable)

def capitalLetter(name):
    return name.upper()
    
family  = ['bhupal','anitha','pujya','havish']
result = map(capitalLetter,family)
print(list(result))

family  = ['bhupal','anitha','pujya','havish']
result = map(lambda name:name.upper(),family)
print(list(result))

# reduce - returns single value
# reduce(function,sequence,initial)

def addAll(a,b):
    return a+b
    
numbers = [20,1,3,10,5]
result = reduce(addAll,numbers)
print(result)

result = reduce(addAll,numbers,1)
print(result)

numbers = [20,1,3,10,5]
result = reduce(lambda a,b:a+b,numbers,11)
print(result)