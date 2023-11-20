text=input("Enter a line of text : ")
words=text.split(" ")
c={}
for t in words:
   if t in c:
     c[t]+=1
   else:
       c[t]=1
print(c)
