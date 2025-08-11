print("select ur ride")
print("1. Bike")
print("2. Car")

choice=int(input("what would you like to select "))
if (choice==1):
    print("1. scooty")
    print("2.royal enfield")
    
    choice2=int(input("select your bike"))
    if (choice2==1):
        print("you have chosen a scooty ")
    else:
        print("you have chosen a royal enfield")
        
elif (choice==2):
    print("select a car")
    print("1. buggati")
    print("2. ferrari")
    
    choice3=int(input("select your car 1"))
    
    if(choice3==1):
        print("you have chosen a buggati")
        
    else:
        print("that you have chosen ferrari🏎️")
        
else:
    print("wrong choice!!!")