n=int(input("enter a number : "))
print(f"multiplication table for {n}:")
for i in range(1,11):
        product=n*i
        print(f"{n}x{i}={product}")
