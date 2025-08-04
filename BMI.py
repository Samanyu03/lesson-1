height=float(input("pls enter ur height in cm"))
weight=float(input("pls enter ur weight in kgs"))

bmi=weight/(height/100)**2

if (bmi<=18.4):
    print("ur are underweight")
    
elif (bmi<=24.9):
    print("ur are healthy")
    
elif (bmi<=29.9):
    print("ur are overweight")
    
elif (bmi<=34.9):
    print("ur are severely overweight ")
    
elif (bmi<=39.9):
    print("ur are obese")
    
else:
    print("ur are severely obese")
    
