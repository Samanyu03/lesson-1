def cube(number):
    return number*number*number

def toys(number):
    if number%3==0:
        return cube(number)
    
    else:
        return False
    
print(toys(12))
print(toys(8))
