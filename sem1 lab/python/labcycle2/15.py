list=input("Enter a list of words separated by spaces : ").split(" ")
longest_length=0
for word in list:
   if(len(word)>longest_length):
      longest_length=len(word)
print("Length of the longest word : ",longest_length)
