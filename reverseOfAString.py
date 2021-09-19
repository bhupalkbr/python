# Reverse of string

#name[start:end:step]
# default - start=0, end=length of string, step=1

name=input("enter a name: ")

print(name)

length = len(name)
print(length)
revstr = name[::-1]

print(revstr)