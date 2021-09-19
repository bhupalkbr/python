#palindrome - string is same even after reversed

name = input("eneter a name: ")

revname = name[::-1]

if (name==revname):
    print("palindrome")
else:
    print("not palindrome")