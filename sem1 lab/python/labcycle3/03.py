input_numbers=input("enter a list of numbers seperated by spaces : ")
numbers=[int(x) for x in input_numbers.split()]
sum_of_items=0
for item in numbers:
        sum_of_items+=item
print("sum of items in the list : ",sum_of_items)

