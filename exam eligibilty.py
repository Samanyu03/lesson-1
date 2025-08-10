a=input("enter your medical cause: ")
ad=int(input("enter your attendence "))

if (a=="Y"):
    print("you are eligible for the exam")
    
else:
    if (ad>=75):
        print("ur ar eeligible for the exam")
        
    else:
        print("you are not eligible for ur exam")