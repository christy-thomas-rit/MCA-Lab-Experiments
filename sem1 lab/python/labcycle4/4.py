def fib(n):
	if n<=1:
		return n;
	else:
		return (fib(n-1)+fib(n-2))
n=int(input("Enter the limit: "))
print("Fibinocci Series : ")
for i in range(n):
	print(fib(i))
