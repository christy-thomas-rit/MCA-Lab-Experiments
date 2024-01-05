def arm(num):
 x=num
 sum=0
 while num>0:
     rem=num%10
     sum=sum+(rem*rem*rem)
     num=num//10
 if sum==x:
   return x
