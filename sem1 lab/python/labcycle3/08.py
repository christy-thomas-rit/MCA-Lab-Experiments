num=int(input("Enter a number : "))
reverse=0
ori=num
while num>0:
	digit=num%10
	reverse=reverse*10+digit
	num=num//10
print("Reverse of",ori,"is",reverse)
