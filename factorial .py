def factorial(x):
    '''this is samanyu coding'''
    if x==1 or x==0:
        return 1
    
    else:
        return x*factorial(x-1)
    
print(factorial.__doc__)
print("the factorial of 5 is: ", factorial(5))
print("the factorial of 4 is: ", factorial(4))
print("the factorial of 3 is: ", factorial(3))
print("the factorial of 2 is: ", factorial(2))
