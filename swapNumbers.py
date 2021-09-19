#program to swap numbers without temporary variable

a,b = input("enter values a & b : ").split(',')

a = int(a)
b = int(b)

a = a+b
b = a-b
a = a-b 

print("b: ",b)
print("a: ",a)