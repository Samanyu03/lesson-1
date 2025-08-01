balance=int(input("please enter your bank balance"))
note1=balance//100
note2=(balance%100)//50
note3=((balance%100)%50)//10

print("the number of 100 rupee note is",note1)
print("the number of 50 rupee note is",note2)
print("the number of 10 rupee note is",note3)
