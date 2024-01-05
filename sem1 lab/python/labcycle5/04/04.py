from Amstrong import arm
l=int(input("Enter the lower limit:"))
u=int(input("Enter the upper limit:"))
print("Armstrong Numbers:")
for i in range(l,u+1):
 if arm(i):
   print(i)
