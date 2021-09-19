#Control Flow program
#program to check the given number is even or odd

'''num=int(input('Enter the number: '))

if(num%2==0):
    print('Even Number')
else:
    print('Odd Number')'''

#shorthand if else
'''num=int(input('Enter the number: '))

print('Even') if(num%2==0) else print('Odd ')'''

    
# program for nested if

'''num = int(input('Enter the number: '))

if (num%2==0):
    if (num%4==0):
        print('yes, Divided by both 2 and 4')
    else:
        print('No, divided by only 2')
        
else:
    print('No, Not divided by both 2 and 4')'''
    
# program for if-elif ladder

rank = int(input('Enter your rank: '))

if rank<=1000:
    print('admission to collegeA')
elif rank>1000 and rank<=10000:
    print('Admission to CollegeB')
elif rank>10000 and rank<=40000:
    print('Admission to collegeC')
else:
    print('No Admission')
    