#factorial of a number

n = int(input("Enter the value: "))
i=1
fact=1
while(i<=n):
    fact=fact*i
    i=i+1
    
print('factorial of {} is {}'.format(n,fact))