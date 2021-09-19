#first non repeated character in a string

name = input("enter string: ")

for i in name:
    if(name.count(i)==1):
        print(i)
        break