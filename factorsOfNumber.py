#factors of a number

n = int(input("enter the number: "))

factors=[]
for i in range(1,n+1):
        if(n%i==0):
            factors.append(i)
            
print(factors)