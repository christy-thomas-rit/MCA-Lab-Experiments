def even_odd(n):
	if n%2==0:
		return 1
	else:
		return 0

n=int(input("Enter a number : "))
evenodd=even_odd(n)
if evenodd==1:
	print(n," is even ")
else:
	print(n," is odd ")
