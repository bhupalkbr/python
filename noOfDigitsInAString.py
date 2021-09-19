#Find number of digits in a string

name = input("Enter string: ")

count=0
for i in name:
    if(i.isdigit()):
        count=count+1
    
print(count)

#can be checked with list also
#numbeers=[0,1,2,3,4,5,6,7,8,9]
