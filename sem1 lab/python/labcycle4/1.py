def simple_inter(name,age):
	p=int(input("Enter principle amount : "))
	n=int(input("Enter no.of years : "))
	if age>60:
		r=12
	else:
		r=10
	si=(p*n*r)/100
	return si

name=input("Enter your name : ")
age=int(input("Enter you age : "))
si=simple_inter(name,age)
print(name,"..Your Simple interest amount is ",si)
