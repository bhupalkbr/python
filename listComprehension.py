#List Comphrensions

numbers = []

for i in range(1,6):
    numbers.append(2**i)
    
print(numbers)  
# same can be written as below in single line

numbers =  [2**i for i in range(1,6)]
print(numbers)

#
import math

numbers = [49, 84,91,100,121]
new_list = [math.sqrt(n) for n in numbers if n%2==0]
print(new_list)

###

team1 = ["janet", "Arya","Mary"]
team2 = ["Evan","Jake", "Randy"]

new_list = [(x,y) for x in team1 for y in team2]

# set comprehension

word = "programming"

alphabets = {x for x in word}
print(alphabets)

# Dictionary comprehension

numbers = [1,2,3,4,5]

square_dict = dict()
for num in numbers:
    square_dict[num] = num**2
    
print(square_dict)

# {1:2,2:4,3:9,4:16,5:25}

# can be written as 
numbers = [1,2,3,4,5]

square_dict = {num:num**2 for num in numbers}
print(square_dict)

#one more example for dictionary comprehension

old_price = {"milk":1.02,"coffee":2.5,"bread":2.5}

new_price = {key: value*1.5 if value>2 else value for (key,value) in old_price.items()}
print(new_price)
