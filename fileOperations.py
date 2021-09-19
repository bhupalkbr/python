#Files operations
#Access modes
#Read Only(r),Write Only(w+),Read and Write(r+), Write and Read(w+), Append Only(a), Append and Read(a+)
# open file - open(filename, accessmode)

#file = open('samplefile.txt','w')
#name = input('Enyter ypur name: ')
#file.write('Welcome {} to file operations'.format(name))
#familyList = ['Bhupal','Aitha','Pujya','Havish']
#file.writelines(familyList)
file1 = open('samplefile.txt','r')
print(file1.read())
file1.close()

with open('samplefile.txt','w') as file:
    file.write('this is using with clause')