# Generate fibnocci series

n = int(input('Enter the n number: '))

n1=0
n2=1
count=0
if(n<=0):
    print('Enter a valid number')
elif(n==1):
    print(n1)
else:
    while(count<n):
        print(n1)
        nextVal=n1+n2
        n1=n2
        n2=nextVal
        count=count+1
        
      