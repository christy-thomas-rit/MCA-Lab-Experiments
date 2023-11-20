l1=input("Enter the values comma separated : ")
l1=[int(x) for x in l1.split(",")]
P_list=[x for x in l1 if x>0]
print("\n LIst Containing only positive numbers : ",P_list)
sq_list=[x**2 for x in l1]
print("\n Square list contains the squares of entered list :",sq_list)
str=input("\nEnter a string : ")
v=[x for x in str if x in 'AaEeIiOoUu']
print("Vowels in String: ",v)
o=[ord(x) for x in str]
print("ASCII values of each char in string ",str,"is",o)
