def str(s1,s2,n):
	for i in range(n):
		if s1[i]==s2[i]:
			r=1
		else:
			r=0
	if(r==1):
		return True
	else:
		return False

s1=input("Enter first string : ")
s2=input("Enter seceond string : ")
n=int(input("Enter a number : "))

result=str(s1,s2,n)
if(result):
	print("Result is Ture\n")
	print("That means first ",n,"character are same ")
else:
        print("Result is False\n")
        print("That means first ",n,"character are not same ")

