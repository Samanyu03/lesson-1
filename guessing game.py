import random
playing=True
a=random.radint(1,100)
print("Welcome to the secret guessing game")

while playing:
    b=int(input("Give me your best guess"))

    if a==b :
        print(f"You guessed the number right, Congratulations!!number was {a}")
        break
    else:
        print("It is not right give me you best guess\n")
