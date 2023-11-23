num=int(input("enter a number : "))

num_copy=num
num_of_digits=0
while num_copy>0:
        num_copy//=10
        num_of_digits+=1
temp=num
armstrong_sum=0

while temp>0:
        digit=temp%10
        armstrong_sum+=digit**num_of_digits
        temp//=10

if num==armstrong_sum:
        print(num,"is an armstrong number.")
else:
        print(num,"is not an armstrong number.")



