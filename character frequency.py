a=input("enter ur own word: ")
b=input("enter a char in the word: ")

i=0
count=0

while (i<len(a)):
    if (a[i]==b):
        count=count+1
        
    i=i+1
    
print("the entered letter has repeated ", count)
    
    
    