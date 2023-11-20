a=int(input("Enter the limit : "))
list=[]
for x in range(0,a):
   string=input("Enter the string : ")
   list.append(string)
count=0
for i in list:
   for j in i:
      if j=="a":
        count+=1
print(count)
