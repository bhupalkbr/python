#Data types program
print('Data Types')

marks = 420
percentage = (marks/600)*100
print('percentage',percentage)
print(type(marks))
print(type(percentage))

x = 10+5j
y = 2+3j
print(type(x))
print(x.real)
print(x.imag)
print(x.conjugate())
print(x+y)

#String Data types
print('=========String Data Types==========')
myName = "Bhupal Reddy Kunduru"
print(myName[0])
print(myName[-2])
print(myName[1:4])
print(myName[5:10:2])
print(myName[::-1])
print("Bhupal" + "Reddy")
print("Bhupal" * 3)
print("Reddy" in myName)
print("hello" not in myName)

#List Data Types
print('==========List=========')
marks=[50,20,90,70,80]
print(type(marks))
print(marks)
family=["Bhupal","Anitha","Pujya","Havish"]
print('family members count: ',len(family))
print(family)
bioDataList = [38,"8939018979","Manikonda",family]
print(bioDataList)
print('second member is: ',family[1])
print('final member is: ',family[-1])
print(bioDataList[3][1])
marks[1]=55
print(marks)
print(marks + family)
print(family * 2)
family.append("Thirupathi")
print(family)
family.extend(["Venkata Reddy","Durgamma"])
print(family)
family.insert(1,"abc")
print(family)
family[1:1]=["a","b","c"]
print(family)
del family[1]
print(family)
family.remove('b')
print(family)
print(family.pop(1))
print(family)

#List Data Types
print('==========Tuple=========')
marks=(20,30,40,50)
print(type(marks))
family=("bhupal","anitha",[20,30,40])
print(type(family))
family[2][1]="dfbgh"
print(family)

print('==========Boolean=========')

a=100
b=100
c=0
print(a==b)
print(type(a==b))
print(bool(a))
print(bool(c))

print('==========Set=========')

friends = {"Sadi","Sunil","Anil","Suresh","Chitti"}
print(type(friends))
emptySet = set()
print(type(emptySet))
print(friends)
friends.add("Sankar")
print(friends)
friends.update(["PVR","Narendra"])
print(friends)
friends.discard("Narendra")
print(friends)
friends.remove("PVR")
print(friends)
friends.discard("ABC")
print(friends)
#friends.remove("ABC")
print(friends)

print("UNION")
a = {10,20,30,40}
b = {50,40,70,80}
abUnion = a.union(b) # a | b
print(abUnion)
abIntersection = a.intersection(b) # a & b
print(abIntersection)
abDifference = a.difference(b) # a - b
print(abDifference)
abSymmetricDifference = a.symmetric_difference(b) # a ^ b
print(abSymmetricDifference)

print("=========Dictionary==============")
bioData={"name":"Bhupal","address":"manikonda"}
print(type(bioData))
information={"lastname":"Kunduru","info":bioData}
print(information)
print(information["lastname"])
print(information.get("lastname"))


D1 = {12:{"class":"BTech","percentage":77.56}
,13:{"class":"BTech","percentage":40.11}
,14:{"class":"BTech","percentage":80.52}
}
print(D1)
rollNumber = int(input("Enter your Roll Number"))
percentage = D1[rollNumber]["percentage"]

if(percentage>50):
    print("pass")
    
else:
    print("fail")
    
information["name"] = "Bhupal Reddy"
print(information)
information["info"]["name"] = "Bhupal Reddy"
print(information)
del information["name"]
print(information)

   
 


