#prime numbers print - number divisible by itself and 1 only

n = int(input("Enter input number: "))

primeNumbers = []
for i in range(2,n+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)
        primeNumbers.append(i)
        
print(primeNumbers)
print(len(primeNumbers))

        
