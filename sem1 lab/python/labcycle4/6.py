l=int(input("Enter the length of rectanlge : "))
b=int(input("Enter the breadth of rectanlge : "))

rect=lambda l,b :l*b
print("Area of reactanle is ",rect(l,b))

a=int(input("\nEnter the length of square : "))
sqr= lambda a : a*a
print("Area of sqaure is ",sqr(a))

h=int(input("\nEnter the height of trianlge : "))
base=int(input("Enter the base of trianlge : "))
tri=lambda h,base :0.5*h*base
print("Area of triangle is : ",tri(h,base))


