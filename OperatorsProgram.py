#Arithmetic Operators
from datetime import date

num1,num2 = input('Enter input values: ').split(',')
a = int(num1)
b= int(num2)

print('addition: ',a+b)
print('subtraction: ',a-b)
print('multiplication: ',a*b)
print('divison: ',a/b)
print('flooring: ',a//b)
print('remainder: ',a%b)
print('power: ',a**b)

yearOfBirth=int(input('Enter your Birth Year'))
currentYear=date.today().year
age=currentYear-yearOfBirth
print(age)