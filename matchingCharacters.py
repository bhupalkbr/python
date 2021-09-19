#program for matching characters

name = input("enter the string: ")

matchingChars=set()
for i in name:
    if (name.count(i)>1):
        matchingChars.add(i)
        
print(matchingChars)