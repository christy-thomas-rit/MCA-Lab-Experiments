l1=input("Enter values comma separated :  " )
l1=[int(x) for x in  l1.split(",")]
l2=input("Enter values comma separated : ")
l2=[int(x) for x in  l2.split(",")]
print(l1)
print(l2)
if len(l1)==len(l2):
  print("Same Length")
else:
    print("Different Length")
if sum(l1)==sum(l2):
  print("Sum are same")
else:
     print("SUm not same")
c=[x for x in l1 if x in l2]
if(c):
  print("common are ",c)
else:
    print("Not Common")
