def add(p, q):
    return p+q

def subtract(p, q):
    return p-q

def multiply(p, q):
    return p*q

def divide(p, q):
    return p/q

print("please enter ur choice ")
print("a. addition")
print("b.subtraction")
print("c.multiplication")
print("d.divide")

choice=input("a/b/c/d: ")
a=int(input("enter ur first number: "))
b=int(input("enter ur second number: "))

if choice == "a" :
    print(add(a,b))
    
elif choice == "b" :
    print(subtract(a,b))
    
elif choice == "c" :
    print(multiply(a,b))
    
elif choice == "d" :
    print(divide(a,b))
    
else:
    print("invalid input!!")