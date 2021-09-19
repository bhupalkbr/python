# ControlflowProgram for loop
import random

'''
numList = [1,2,30,35,50,70]

for num in numList:
    print(num)
    
name = "Bhupal Reddy"

for character in name:
    print(character)
    
for item in range(10):
    print(item)
    
for item in range(10,0,-1):
    print(item)
  
name = input('enter your name')
 
lastTwoChars = name[-2:]
 
for i in range(1,11):
    print(lastTwoChars*i)
    
numDict = {1:"One",2:"Two",3:"Three"}

for i in numDict:
    print(i)
    print(numDict[i]) '''
    
name = input('Enter your name')
 
vowelsList = ['a','e','i','o','u']
 
for i in name:
    if i in vowelsList:
        print(i, ' - Vowel')
        break
    else:
        print(i, ' - Consonant')
        
marks = [20,30,40,50,60]

sum = 0
for mark in marks:
    sum = sum + mark

print("Total: ", sum)

#while loop
i = 1

while i<10:
    print(i)
    i=i+1
    
print(random.randint(1,30))

score = 0
scoreInfo = []
while score<500:
    scoreValue = random.randint(1,30)
    score = score + scoreValue
    scoreInfo.append(scoreValue)
    
print('Total Flips: ', len(scoreInfo), scoreInfo)
