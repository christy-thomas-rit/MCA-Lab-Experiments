file = open("File1.txt","r")
file2 = open("File2.txt","w")
line = file.readlines()
lis=[]
for i in range(len(line)):
        if(i%2!=1):
                file2.write(line[i])
                lis.append(line[i])

print("Odd Lines that are copied from one file to another : \n",lis)
file.close()
file2.close()
