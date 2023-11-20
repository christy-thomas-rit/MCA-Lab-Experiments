color_list1=input("Enter the first list : ").split(" ")
color_list2=input("Enter the second list : ").split(" ")
result=[item for item in color_list1 if item not in color_list2]
print("values from color_list1 not contained in color_list2 : ",result)

