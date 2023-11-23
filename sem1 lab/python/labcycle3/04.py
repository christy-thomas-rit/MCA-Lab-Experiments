start_range=int(input("Enter the start of the range : "))
end_range=int(input("Enter the end of the range : "))
result_list=[]
for num in range(start_range,end_range+1):
	if 1000<=num<=9999:
		if all(int(digit)%2==0 for digit in str(num)):
			sqrt=int(num**0.5)
			if sqrt*sqrt==num:
				result_list.append(num)
print("Four digit perfect square number with all even digits within the specified range: ")
print(result_list)
