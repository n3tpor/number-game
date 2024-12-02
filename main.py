import random

while True:
    number = random.randint(1,10)
    userGuess = input("I have a number between 1 and 10 (inclusive), guess what the number is!")
    if number == int(userGuess):
        print("Correct!")
    else:
        print(f"Wrong! The number was {number}")
    
