num= int(input("enter a number: "))

factor=1
print("factors of",num,"are: ")

while factor<=num:
        if num%factor==0:
                print(factor)
        factor+=1
