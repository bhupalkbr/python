#number of vowels & consonants
name=input("Enter the string: ")

vowels=['a','e','i','o','u']

vowelsList=[]
consonantsList=[]

for i in name:
    if(i in vowels):
        vowelsList.append(i)
        
    else:
        consonantsList.append(i)


print(vowelsList)
print(consonantsList)
       
vowelsCount=len(vowelsList)
consonantsCount=len(consonantsList)

print('vowels count is {} and consonants count is {}'.format(vowelsCount,consonantsCount))