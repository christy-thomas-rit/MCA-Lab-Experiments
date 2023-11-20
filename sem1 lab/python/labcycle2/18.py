dict1={}
dict2={}
n=int(input("Enter the number of values : "))
for i in range(n):
   name=input("Enter name : ")
   age=int(input("Enter age : "))
   dict1[name]=age
for i in range(n):
   place=input("Enter place : ")
   dis=int(input("Enter distance : "))
   dict2[place]=dis
dict1.update(dict2)
print(dict1)

