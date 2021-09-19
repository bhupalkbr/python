#reverse number

135


n = int(input("Enter number: "))
input_num=n
revnum=0

while(n>0):
    
    i=n%10
    revnum = revnum*10 + i
    n=n//10
    
print('reversed number for {} is {}'.format(input_num,revnum))