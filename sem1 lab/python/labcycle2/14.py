str=input("Enter a String : ")
if(str.endswith("ing")):
   str=str+"ly"
else:
     str=str+"ing"
print("Modified Word : ",str)
