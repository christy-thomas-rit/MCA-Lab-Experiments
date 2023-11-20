x=[]
n=int(input("Enter the no of elements in the list : "))
for i in range(n):
   a=int(input("Enter the value : "))
   if a<100:
     x.append(a)
   else:
       x.append("over")
print(x)
    
