def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)

def series(n):
    sum = 0
    for i in range(1, n + 1):
        term = i ** i / fact(i)
        sum =sum+ term
    return sum

n = int(input("Enter the value of n : "))
if(n>=0):
	result = series(n)
	print(f"The sum of the series is: {result}")
else:
	print("Invalid input. Please enter a valid integer.")
