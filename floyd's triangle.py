n=1
a=int(input("Enter the number of rows: "))

for i in range(a):
    for j in range(i+1):
        print(n ,end=" ")
        n=n+1
    print()