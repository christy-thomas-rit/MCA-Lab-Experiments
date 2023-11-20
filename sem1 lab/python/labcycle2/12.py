list=input("Enter the value : ").split(",")
list=[int(item)for item in list]
remove=[i for i in list if i%2!=0]
print("Original List : ",list)
print("New List without even numbers : ",remove)
