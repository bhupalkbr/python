#To demomnstrate input & output

pin,cash = input('Enter the pin and amount: ').split(',')
print('pin & cash are : ',pin,cash)
withDrawAmount=int(cash)
#print('Type of cash is : ',type(cash))
totalAmount = 50000
remainingAmount = totalAmount-withDrawAmount

#print('Take your cash',cash,remainingAmount,sep="->",end="==>")
print('Take your cash {}, The balance in your account is {}'.format(withDrawAmount,remainingAmount))
print('Thank you',end="\t")
print('End of Second Program')
