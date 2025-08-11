str1=input("enter a string for its reverse value : ")
str2=("")

for i in str1:
    str2=i+str2
    
print("the original form : ", str1)
print("the reversed form : ", str2)