#this is my first python program
print('welcome to python')

sum = 10
def calculate():
    global sum
    sum = sum + 20
    currenrSum = 200
    totalSum=sum+currenrSum
    print(totalSum)
    
calculate();
print(sum)