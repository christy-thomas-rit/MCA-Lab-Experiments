N=int(input("Enter the number of steps : "))
for i in range(1,N+1):
	for j in range(1,i+1):
		step_number=i*j
		print(step_number,end=" ")
	print()
