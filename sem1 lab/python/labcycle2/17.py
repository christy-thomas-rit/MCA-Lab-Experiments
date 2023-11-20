myDict={}
n=int(input("Enter the number of values : "))
for i in range(n):
   name=input("Enter the name : ")
   age=input("Enter the age : ")
   myDict[name]=age
mykeys=list(myDict.keys())
mykeys.sort()
asce={i:myDict[i] for i in mykeys}
mykeys.sort(reverse = True)
desc={i:myDict[i] for i in mykeys}
print("Ascending : ",asce)
print("Descending : ",desc)
