#Armstrong - 
# eg: 153 ---- 1^3+5^3+3^3 = 153 is a armstrong

n =input("enter the value: ")
intnum=int(n)
originalVal=intnum
revnum=0
print(pow(intnum,3))
for i in n:
    i=int(i)
    revnum = revnum + i**3
    
if intnum==revnum:
    print("armstrong")
else:
    print("not armstrong")
    

revnumx=0

while (intnum>0):

    i=intnum%10
    print(i)
    revnumx=revnumx + i**3
    intnum=intnum//10


print(revnumx)   
if originalVal==revnumx:
    print("armstrong")
else:
    print("not armstrong")
    
 